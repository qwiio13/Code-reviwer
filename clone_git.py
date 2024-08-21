from git import Repo
import os
import shutil


def clone_rep(repo_url, clone_dir):
    # сheck if the directory is empty, and clear it if it’s not
    if os.listdir(clone_dir):
        shutil.rmtree(clone_dir)
        os.makedirs(clone_dir)
    print(f"Dir '{clone_dir}' was clear.")
    # clone repo
    Repo.clone_from(repo_url, clone_dir)
    print(f"Repo was cloned successfully in {clone_dir}")
