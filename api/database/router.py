class ReadWrite:
    """
    Handles all models associated with the respected database.
    """

    def db_for_read(self, model, **hints):
        """
        Attempts to read models go to 'default_read1'.
        """

        return 'default_read1'

    def db_for_write(self, model, **hints):
        """
        Attempts to write models go to 'default' database.
        """

        return 'default'

    def allow_relation(self, obj1, obj2, **hints):
        """
        Allow relations.
        """

        return True

    def allow_migrate(self, db, app_label, model_name=None, **hints):
        """
        Allow migrations.
        """

        return db == 'default'
