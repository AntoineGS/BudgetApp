from app import db
from app.main import bp
from flask import render_template, flash, redirect, url_for, request, g, jsonify
from flask_login import current_user, login_required


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