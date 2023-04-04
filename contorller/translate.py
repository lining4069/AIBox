from flask import render_template, Blueprint, request

translate = Blueprint('translate', __name__)


@translate.route('/translate/api2d')
def translate_api2d_index():
    return render_template()


@translate.route('/translate/api2d/process')
def translate_api2d_process():
    user_text_in_lan = request.args.get('language_input')
    user_text_out_lan = request.args.get('language_return')
    user_text = request.args.get('msg')

