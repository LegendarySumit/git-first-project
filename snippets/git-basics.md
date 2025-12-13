## 1. Git Fundamentals (Conceptual Overview)

```
git init
git status
git add .
git add <file>
git commit -m "message"
git log --oneline
git push origin main
git pull origin main
```

## 2. Branching and Merging 

```
git branch
git branch feature/login
git checkout feature/login
git checkout -b feature/signup
git merge feature/login
git branch -d feature/login
```

## 3. Stashing Changes 
```
git stash
git stash list
git stash pop
```

## 4. Remote Repositories and Tags 

```
git pull
# resolve conflicts manually
git add .
git commit -m "Resolve merge conflict"
```

## 5. Tags and Releases
```
git tag
git tag v1.0.0
git tag -a v1.1.0 -m "Release version 1.1.0"
git push origin v1.0.0
git push --tags
```

## 6. Forking and Upstream Syncing
```
git clone <repo-url>
git remote -v
git remote add upstream <original-repo-url>
git fetch upstream
git merge upstream/main
```

## 7. Cherry-Picking Commits
```
git cherry-pick <commit-hash>
```
