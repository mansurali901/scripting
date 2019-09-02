class Config:

    def local(self):
        return {
            "temp_dir": "/tmp/dirtest/",
            "devops": "Mansur",
        }

    def stg(self):
        return {}
    

    def prod(self):
        return {}