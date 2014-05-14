from . import transcode

@transcode.route('/')
def home():
    return 'Hello app'

@transcode.route('/jobs')
def get_jobs():
    return 'Hello get_jobs'

@transcode.route('/jobs', methods=['POST'])
def post_newjob():
    return 'Hello post_newjob'

@transcode.route('/jobs/<int:id>/')
def get_jobstatus(id):
    return 'Hello get_jobstatus: %d' % id

@transcode.route('/jobs/purge/<int:age>/', methods=['DELETE'])
def purge_jobs(age):
    return 'Hello purge_jobs : %d' % age

@transcode.route('/jobs/<int:id>/', methods=['DELETE'])
def remove_job(id):
    return 'Hello remove_job: %d' % id

@transcode.route('/probe/', methods=['POST'])
def probe_file():
    return 'Hello probe_file'
