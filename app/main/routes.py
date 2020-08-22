from app import db
from app.main import bp, refresh_bank as rb
from app.main.forms import NewCategoryForm
from app.models import Category
from flask import render_template, jsonify, redirect, url_for, request
from flask_login import login_required
import json


@bp.route('/', methods=['GET', 'POST'])
@bp.route('/index', methods=['GET', 'POST'])
@login_required
def index():
    return render_template('index.html', title='Home')


@bp.route('/refresh_bank', methods=['POST'])
@login_required
def refresh_bank():
    count = rb.refresh_bank()
    return str(count)


@bp.route('/categories',  methods=['GET', 'POST'])
@login_required
def categories():
    form = NewCategoryForm()
    if form.is_submitted():
        if form.validate_on_submit():
            category = Category(name=form.category_name.data, use_in_budget=form.use_in_budget.data)
            db.session.add(category)
            db.session.commit()
            return jsonify(status='ok')
        else:
            # data = json.dumps(form.errors, ensure_ascii=False)
            data = json.dumps(form.errors, ensure_ascii=False)
            return jsonify(data)
    categories_records = Category.query.order_by(Category.name.asc()).all()
    return render_template('categories.html', title='Categories', category_form=form, categories=categories_records)


@bp.route('/categories/edit/<category_id>',  methods=['GET', 'POST'])
@login_required
def categories_edit(category_id):
    category = Category.query.get_or_404(category_id)
    form = NewCategoryForm()
    if form.is_submitted():
        if form.validate_on_submit():
            if 'submit' in request.form:
                category.name = form.category_name.data
                category.use_in_budget = form.use_in_budget.data
                db.session.commit()
        return redirect(url_for('main.categories'))
    else:
        form.fill_from_db(category)
    return render_template('category.html', title='Edit Category', category_form=form)


@bp.route('/categories/delete/<category_id>',  methods=['GET', 'POST'])
@login_required
def categories_delete(category_id):
    category = Category.query.get(category_id)
    if category:
        db.session.delete(category)
        db.session.commit()
        return jsonify(status='ok')
    else:
        return jsonify(status='not_found')
