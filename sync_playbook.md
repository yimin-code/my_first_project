# Refined Git Multi-Device Sync Playbook

This guide serves as the source of truth for keeping your iMac and MacBook perfectly synced, authenticated, and configured for your bioinformatics pipelines.

---

## 1. Initial Setup & Cloning
When downloading your code for the first time on a new machine, let Git handle the folder creation:
* Navigate to your working directory: `cd ~/Python`
* Run the clone command: `git clone https://github.com/USERNAME/my_first_project.git`
* Git will automatically generate the project folder for you.

---

## 2. Git Configuration (Identity)
Git needs to know who is making changes so it links commits to your profile. **Run this on both your iMac and MacBook.**

* **Check your current settings:**
  ```bash
  git config user.name
  git config user.email
  ```
* **Set your identity (if blank):**
  ```bash
  git config --global user.name "Your Name"
  git config --global user.email "your.email@example.com"
  ```
  *(Note: The email must match your GitHub account).*

---

## 3. Modern Authentication (VS Code OAuth)
Because VS Code handles authentication via secure browser-based OAuth web flows:
* **How it works:** When prompted to login via the terminal or VS Code, it will open your browser. Approving it grants a secure, encrypted token stored automatically in your Mac's **Keychain Access**.
* **Device Independence:** Both your iMac and MacBook can be logged into the same GitHub account simultaneously without interfering with each other.

---

## 4. Essential Project Hygiene (`.gitignore`)
Always maintain a master `.gitignore` file in your root folder to prevent cluttering GitHub with local system files or environments. 

**Standard Python & Mac `.gitignore` Template:**
```text
# Ignore Mac system files
.DS_Store

# Ignore VS Code workspace settings
.vscode/

# Ignore Python virtual environments and cache
.venv/
__pycache__/
```

---

## 5. Daily Sync Workflow (The Golden Rule)

Always sync your environment **before** you start coding, and push **after** you finish.

### When starting work (Pull):
```bash
git pull
```

### When finishing work (Push):
1. Check your status (yellow/green files):
   ```bash
   git status
   ```
2. Stage your changes:
   ```bash
   git add .
   ```
3. Commit with a descriptive message:
   ```bash
   git commit -m "Describe your changes here"
   ```
4. Push to the cloud:
   ```bash
   git push
   ```

