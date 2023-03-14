from uuid import uuid4

def upload_image_formater(instance, filename):
    print(instance)
    return f'{str(uuid4())}-{filename}' 