from app import app

@app.route('/')
def home():
    return 'Hello app'

@app.route('/jobs')
def get_jobs():
    return 'Hello get_jobs'

@app.route('/jobs', methods=['POST'])
def post_newjob():
    return 'Hello post_newjob'

@app.route('/jobs/<int:id>/')
def get_jobstatus(id):
    return 'Hello get_jobstatus: %d' % id

@app.route('/jobs/purge/<int:age>/', methods=['DELETE'])
def purge_jobs(age):
    return 'Hello purge_jobs : %d' % age

@app.route('/jobs/<int:id>/', methods=['DELETE'])
def remove_job(id):
    return 'Hello remove_job: %d' % id

@app.route('/probe/', methods=['POST'])
def probe_file():
    return 'Hello probe_file'
