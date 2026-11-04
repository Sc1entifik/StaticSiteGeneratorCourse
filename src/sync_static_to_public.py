import os
import shutil

def sync_static_to_public(source, destination):
    if os.path.exists(destination):
        shutil.rmtree(destination)

    os.mkdir(destination)

    directories_stack = [(source, destination)]

    while directories_stack:
        current_source, current_destination = directories_stack.pop()

        for item in os.listdir(current_source):
            source_path = os.path.join(current_source, item)
            destination_path = os.path.join(current_destination, item)

            if os.path.isfile(source_path):
                print(f"Copying {source_path} to {destination_path}\n")
                shutil.copy(source_path, destination_path)

            else:
                os.mkdir(destination_path)
                directories_stack.append((source_path, destination_path))
