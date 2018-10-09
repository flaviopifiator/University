import os


def upload_to(instance, filename):
    opts = instance.content_object._meta
    upload_dir = os.path.join(
        opts.app_label,
        '%s_%s' % (opts.model_name, instance.content_object.pk)
    )
    
    if not os.path.exists(upload_dir):
        os.makedirs(upload_dir)
    return os.path.join(upload_dir, filename)