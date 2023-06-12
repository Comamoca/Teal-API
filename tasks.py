from invoke import task

@task
def dev(c):
    """Launch dev server"""
    c.run("rye run uvicorn main:app --reload")
