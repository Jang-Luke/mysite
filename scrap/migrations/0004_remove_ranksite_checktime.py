from django.db import migrations


class Migration(migrations.Migration):
    
    dependencies = [
        ('scrap', '0003_alter_ranksite_checktime'),
    ]
    
    operations = [
        migrations.RunSQL(
            sql = "ALTER TABLE luke_db.scrap_ranksite DROP COLUMN checkTime CASCADE"
        )
    ]