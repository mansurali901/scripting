class Config:

    def locations(self):
        return {
            "Stage_backup_dir": "/tmp/dirtest/",
            "Prod_backup_dir": "/tmp/backupprod/",
        }

    def username(self):
        return {
            "stage_username": "stage",
            "prod_username": "prod",
        }
    

    def password(self):
        return {
            "stage_password": "abc123+",
            "prod_password": "ABC123+",
        }