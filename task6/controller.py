from flask import Flask, render_template
from flask_codemirror import CodeMirror
from task6 import service
from flask_wtf import FlaskForm
from flask_codemirror.fields import CodeMirrorField
from wtforms.fields import SubmitField


class MyForm(FlaskForm):
    source_code = CodeMirrorField(language='sql', config={'lineNumbers': 'true'})
    submit = SubmitField('Submit')


CODEMIRROR_LANGUAGES = ['sql', 'python', 'htmlembedded']
WTF_CSRF_ENABLED = True
SECRET_KEY = 'secret'
app = Flask(__name__)
app.config.from_object(__name__)
codemirror = CodeMirror(app)


@app.route('/', methods=['GET', 'POST'])
def root():
    form = MyForm()
    response = None
    if form.validate_on_submit():
        response = service.execute_query(form.source_code.data)
    if response is not None:
        if len(response.error) != 0:
            return render_template('error.html', error=response.error, form=form)
        return render_template('index.html', column_names=response.columns, data=response.data, form=form)
    return render_template("index.html", form=form)


if __name__ == '__main__':
    app.run()
