# coding: utf-8
from flask import render_template, Blueprint
from ..models import Blog, Post

bp = Blueprint('site', __name__)


@bp.route('/')
def index():
    """首页"""
    blogs = Blog.query
    latest_posts = Post.query.order_by(Post.created_at.desc()).limit(10)
    latest_blogs = Blog.query.order_by(Blog.created_at.desc()).limit(10)
    return render_template('site/index.html', blogs=blogs, latest_posts=latest_posts,
                           latest_blogs=latest_blogs)


@bp.route('/about')
def about():
    """关于页"""
    return render_template('site/about.html')