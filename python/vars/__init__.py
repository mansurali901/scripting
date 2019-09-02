class Config:

    def local(self):
        return {
            "backup_dir": "/tmp/dirtest/",
            "devops": "Mansur",
        }

    def stg(self):
        return {}
    

    def prod(self):
        return {}