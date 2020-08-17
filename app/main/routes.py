from app import db
from app.main import bp, refresh_bank as rb
from app.main.forms import NewCategoryForm
from app.models import Category
from flask import render_template, flash, redirect, url_for, request, jsonify
from flask_login import login_required
import json


@bp.route('/', methods=['GET', 'POST'])
@bp.route('/index', methods=['GET', 'POST'])
@login_required
def index():
    # form = PostForm()
    # if form.validate_on_submit():
    #     post = Post(body=form.post.data, author=current_user, language=language)
    #     db.session.add(post)
    #     db.session.commit()
    #     flash('Your post is now live!')
    #     return redirect(url_for('main.index'))
    # page = request.args.get('page', 1, type=int)
    # posts = current_user.followed_posts().paginate(
    #     page, config.postsPerPage, False)
    # next_url = url_for('main.index', page=posts.next_num) \
    #     if posts.has_next else None
    # prev_url = url_for('main.index', page=posts.prev_num) \
    #     if posts.has_prev else None
    # return render_template('index.html', title=_('Home'), form=form,
    #                        posts=posts.items, next_url=next_url,
    #                        prev_url=prev_url)
    return render_template('index.html', title='Home')


@bp.route('/refresh_bank', methods=['POST'])
@login_required
def refresh_bank():
    count = rb.refresh_bank()
    return str(count)


@bp.route('/categories',  methods=['GET', 'POST'])
@login_required
def categories():
    form = NewCategoryForm()  # for rendering only, the processing is in add-directory
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
    return render_template('categories.html', title='Categories', category_form=form)
