from pydriller import Repository
import pandas as pd

# Update to local clone path of Airbnb JavaScript repo
repo_path = "./flask"  # change this to your local path where repo is cloned

data = []
keywords = [
    "fixed ", " bug", "fixes ", "fix", "fix", " fixed", " fixes", "crash", "solves", " resolves", "resolves", 
    "issue", "issue ", "regression", "fall back", "assertion", "coverity", "reproducible", "stack-wanted", 
    "steps-wanted", "testcase", "failur", "fail", "npe ", " npe", "except", "broken", "differential testing", 
    "error", "hang ", " hang", "test fix", "steps to reproduce", "crash", "assertion", "failure", "leak", 
    "stack trace", "heap overflow", "freez", "problem", "problem", "overflow", "overflow ", "avoid ", "avoid", 
    "workaround ", "workaround", "break", "break", "stop", "stop"
]

for commit in Repository(repo_path).traverse_commits():
    msg = commit.msg.lower()
    if any(keyword in msg for keyword in keywords):
        data.append([
            commit.hash,
            commit.msg,
            commit.parents,  # fixed here
            commit.merge,
            [mod.new_path for mod in commit.modified_files]
        ])

df = pd.DataFrame(data, columns=["Hash", "Message", "Hashes of parents", "Is a merge commit?", "List of modified files"])
df.to_csv("bug_fixing_commits.csv", index=False)
print(f"Extracted {len(df)} bug-fixing commits.")
