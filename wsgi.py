from api import create_app, db
from api.model import Admins, Students

app = create_app("staging")


#   configure shell feature to query database from shell

@app.shell_context_processor
def make_shell_context():
    return dict( db=db, Admins=Admins, Students=Students)



