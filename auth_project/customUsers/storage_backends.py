from storages.backends.s3boto3 import S3Boto3Storage, SpooledTemporaryFile
import os

# class CustomS3Boto3Storage(S3Boto3Storage):
#     location = 'media'
#     default_acl = 'public-read'
#     #file_overwrite = False





class StaticStorage(S3Boto3Storage):
    location = 'static'
    default_acl = 'public-read'


class PublicMediaStorage(S3Boto3Storage):
    location = 'media'
    default_acl = 'public-read'
    #file_overwrite = False

    def _save(self, name, content):
        """
        We create a clone of the content file as when this is passed to boto3 it wrongly closes
        the file upon upload where as the storage backend expects it to still be open
        """
        # Seek our content back to the start
        content.seek(0, os.SEEK_SET)

        # Create a temporary file that will write to disk after a specified size
        content_autoclose = SpooledTemporaryFile()

        # Write our original content into our copy that will be closed by boto3
        content_autoclose.write(content.read())

        # Upload the object which will auto close the content_autoclose instance
        super(PublicMediaStorage, self)._save(name, content_autoclose)
        # Cleanup if this is fixed upstream our duplicate should always close
        if not content_autoclose.closed:
            content_autoclose.close()