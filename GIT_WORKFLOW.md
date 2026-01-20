# Git Workflow Documentation

## Branching Strategy 
`main` will always hold production-ready code. Every change, whether a feature, bug fix, or spelling error shouldbe developed on a separate branch. Only updates will come from merged pull requests 

Branch names should be lowercase and use hyphens to separate words. 

### Branch Types 
The following branch types will be utilized for the branching strategy 

### 1. Main branch (`main`)
- Production-ready code 
- Stable and deployable 
- Updated only through merged pull requests 

### 2. Feature Branches (`/feature`)
- Developing features or functionality 
- Deleted after merge 
- Naming convention: `feature/descriptive-name`

### 3. Hotfix Branches
- Temporary branches to quickly fix urget issues 
- Deleted after merge 
- Naming convention: `hotfix/descriptive-name`

## Commit message conventions 
Follow [convential commits](https://www.conventionalcommits.org/en/v1.0.0/) format:
```
<type>: <subject>

<body (optional)>

<footer (optional)>
```

## Code Review Process 
After pushing create pull request which contains the following:
- What does the change do?
- Why is this change needed? Provide context.
- How is the change tested? Provide information to the reviewer that the change does indeed work.
- Insert screenshots if applicable.

## Release Workflow
0. Ensure you are on the latest version of `main`.
1. Create a new branch off of `main`.
2. Implement changes and push commits along the way.
    - Pushing often and early to ensure that the most up to date code is on Github. Meaning push after every commit or pushing after you stop a work session 
3. When code is ready for review open a pull request.
4. Once reviewed, merge branch into `main` and delete branch.


## GIT Commands Reference 

### Daily commands
```sh
git status              # Check current state
git add .               # Stage all changes
git commit -m "msg"     # Commit changes
git push                # Push to remote
git pull                # Pull from remote
```

### Starting new work
```sh
git checkout main
git pull origin main
git checkout -b feature/new-feature
```

###
### Finishing Work
```sh
git add .
git commit -m "feat: Add new feature"
git push -u origin feature/new-feature
# Create pull request on GitHub
```

## Sources 
- Majority if not at all of the git workflow standards shown here come from [dev-handbook](https://github.com/Clever/dev-handbook/blob/master/git-workflow.md)