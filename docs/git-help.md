# Git Quick Help Guide

A beginner-friendly guide to Git terminologies and the most common commands.

---

## 1. Core Terminologies

| Term | Description |
|------|-------------|
| **Repository (Repo)** | Your project's folder, including the hidden `.git` folder that tracks history. |
| **Commit** | A "snapshot" of your changes at a specific point in time. Like a save point. |
| **Staging Area (Index)** | A middle ground where you pick which changes to include in the next commit. |
| **Branch** | An independent line of development. The default branch is usually called `main`. |
| **Merge** | Combining changes from one branch into another (e.g., merging a feature into main). |
| **Remote** | A version of your repository hosted on a server (like GitHub, GitLab, or Bitbucket). |
| **Clone** | Creating a local copy of a remote repository on your computer. |
| **Pull** | Fetching changes from a remote repository and merging them into your local work. |
| **Push** | Sending your local commits to a remote repository. |

---

## 2. Basic Workflow Commands

### Initializing and Cloning
```bash
# Turn a local folder into a Git repo
git init

# Copy an existing repo from a URL
git clone <url>
```

### Tracking Changes
```bash
# Check the status of your files (which are changed, staged, etc.)
git status

# Add a specific file to the staging area
git add filename.py

# Add all changed files to the staging area
git add .

# Save your staged changes with a descriptive message
git commit -m "Add new feature for user login"
```

### Syncing with Remote
```bash
# Upload your local commits to the server
git push origin main

# Download the latest changes from the server
git pull origin main
```

---

## 3. Working with Branches

Branches allow you to work on new features without breaking the "main" code.

```bash
# List all local branches
git branch

# Create a new branch
git branch feature-name

# Switch to a branch
git checkout feature-name
# or (modern way)
git switch feature-name

# Create AND switch to a new branch in one command
git checkout -b feature-name
# or (modern way)
git switch -c feature-name

# Merge a branch into your current branch
git merge feature-name
```

---

## 4. History and Undoing

```bash
# See a list of previous commits
git log

# See a simplified one-line version of history
git log --oneline

# Unstage a file (keep the changes but don't commit yet)
git reset filename.py

# Discard local changes in a file (revert to last commit)
git checkout -- filename.py
```

---

## 5. The Standard Daily Workflow

1. **Pull** latest changes from others: `git pull origin main`
2. **Create** a branch for your work: `git checkout -b my-task`
3. **Write** code and save.
4. **Stage** your work: `git add .`
5. **Commit** your work: `git commit -m "Complete my task"`
6. **Push** to the server: `git push origin my-task`

---

## Common Questions

**Q: What is the difference between `git add` and `git commit`?**
A: `git add` picks which files go into the "box." `git commit` closes the box and puts a label on it.

**Q: What is a "Merge Conflict"?**
A: This happens when two people change the same line of the same file. Git gets confused and asks you to manually choose which version to keep.

**Q: Why use branches?**
A: So you can experiment or fix bugs without affecting the "stable" version of the project that others are using.
