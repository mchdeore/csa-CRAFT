# Team Setup Guide: VS Code + Claude Code + GitHub

Two parts:

1. Why GitHub (read first)
2. Setup (follow in order)

---

## Part 1 -- GitHub Suggestion

A shared Git repository (like my demo scratchpad repo) would let everyone build on the same application through their own branches while still making independent progress. They could directly work off of my project in branches to contribute to the AI web app I'm making for Hany and integrate your aspects directly.

Team members could develop features, experiments, scripts, synthetic datasets, and other assets in a place that's visible to the whole team and easy to integrate.

This would also solve the problem of people sending work through multiple channels. Instead, code, data, documentation, and supporting files would all live in one central location that can be reviewed, reused, and merged as needed.

An added benefit is that contributors could use VS Code and AI-assisted development directly against the project, enabling much more powerful workflows for scripting, data analysis, automation, and large-scale file processing than what is currently possible in our browser-based setup (sorting through data lake, reformatting docs, etc).

We can deploy everything as one item on Azure off of a version-controlled repo (GitHub temporary fix -- Azure native version control once development progresses).

Users can experiment with more powerful AI workflows, help the development team identify common use cases worth investigating as sophisticated solutions, and even build such solutions themselves or test them out as first users.

This is better than everyone working through Azure directly. We get our own page on our own route, AI can assist each person, and a more senior developer can be in charge of merging code into final access-restricted branches. Users can be confined to their own branch, receiving a code update whenever a new deployment is pushed out.

Tools and skills can be set up to help Claude perform repository access actions, code workflows to help users work on their pages with user-specific knowledge-scoped responses and questions, etc.

---

## Part 2 -- Setup

Prerequisites: Windows machine, internet connection, npm installed. (If you don't have npm, ask IT -- a few people on the team got it from them.)

---

### Step 1 -- Install VS Code

Download: https://code.visualstudio.com/download

Run installer. Check these boxes:

- [ ] "Add 'Open with Code' action to Windows Explorer file context menu"
- [ ] "Add 'Open with Code' action to Windows Explorer directory context menu"

Leave everything else at defaults.

VS Code opens. Close every tab and popup. Window should be empty.

---

### Step 2 -- Open your workspace and terminal

Create a folder on your Desktop. Name it whatever you want.

In VS Code:

```
Ctrl + K, Ctrl + O
```

Pick your folder. Click "Select Folder". Click "Yes, I trust the authors".

Open terminal:

```
Ctrl + `
```

---

### Step 3 -- Install Claude Code

```
npm config set allow-scripts=@anthropic-ai/claude-code --location=user
npm install -g @anthropic-ai/claude-code
```

No output on first line. Second line takes 1-2 minutes. No errors = done.

---

### Step 4 -- Set up Microsoft Foundry

If someone gave you an API key, skip to 4c.

**4a. Create resource.** In Microsoft Foundry portal, create a resource. Write down its name.

**4b. Create deployments.** Create three: `claude-opus`, `claude-sonnet`, `claude-haiku`.

**4c. Set API key.** Copy key from Foundry -> Endpoints and keys. In terminal:

```
setx ANTHROPIC_FOUNDRY_API_KEY "paste-your-key-here"
```

Close terminal tab, open new one with `Ctrl + ``. Confirm:

```
echo %ANTHROPIC_FOUNDRY_API_KEY%
```

Should print your key. If blank, close and reopen VS Code.

**Alternative:** If you have Azure CLI:

```
az login
```

---

### Step 5 -- Run Claude health check

```
claude doctor
```

This checks Claude can talk to Foundry, read files, and run commands. Fix anything it flags.

If Claude itself won't start or `/doctor` fails -- open Claude chat sidebar (`Ctrl + Shift + I`), paste the error, say:

```
I am on Windows with npm installed. This error happened. What do I do?
```

---

### Step 6 -- Install Git

Download: https://git-scm.com/download/win

Run installer. Click Next for everything. Do not change defaults.

Close VS Code. Reopen.

```
git --version
```

Should print `git version 2.46.0` or similar. If error, close VS Code and reopen.

---

### Step 7 -- Create a GitHub account

Go to https://github.com/signup

Use work email. Pick username and password. Skip all questions.

---

### Step 8 -- Let Claude handle GitHub setup

```
Ctrl + Shift + I
```

Paste this:

```
Connect this machine to my GitHub account and clone the project repo.
Walk me through one step at a time. Tell me what to type, wait for me
to confirm. If anything fails, explain in plain language and give the fix.

My name: [YOUR NAME]
My email: [YOUR EMAIL]
Project URL: [URL FROM MARCUS]

I need:
1. Git config with my name/email
2. SSH key for GitHub
3. Add SSH key to my GitHub account
4. Clone the project
5. Create my personal branch
6. Show me how to save, push, and pull

Windows. npm and git installed. First time doing this.
```

Replace bracketed parts. Claude walks you through each step.

---

### Step 9 -- Confirm it worked

```
git config user.name
git config user.email
git branch
git remote -v
```

Should print your name, your email, your branch with a star, and the project URL.

---

## Everyday workflow

| Action | Command |
|--------|---------|
| Pull latest | `git pull origin main` |
| Your branch | `git checkout your-name/my-work` |
| Save work | `git add .` then `git commit -m "what you did"` |
| Upload | `git push origin your-name/my-work` |
| See other branch | `git fetch origin` then `git checkout branch-name` |

---

## If anything breaks

1. Paste error into Claude chat (`Ctrl + I` or `Ctrl + Shift + I`).
2. Say: "Windows, npm installed. What does this mean and what do I type?"
3. If Claude can't fix it, search the error on GitHub (https://github.com -- paste the error into the search bar).
4. If still stuck, message Marc Chedore on Teams.

---

## Keyboard shortcuts

| Keys | Does |
|------|------|
| `Ctrl + `` | Terminal |
| `Ctrl + Shift + P` | Search any command |
| `Ctrl + P` | Open file |
| `Ctrl + S` | Save |
| `Ctrl + K, Ctrl + O` | Open folder |
| `Ctrl + I` | Claude chat (inline) |
| `Ctrl + Shift + I` | Claude chat (sidebar) |

---

## Checklist

- [ ] VS Code opens to empty window
- [ ] `Ctrl + `` opens terminal
- [ ] Claude installed, `/doctor` passes
- [ ] `echo %ANTHROPIC_FOUNDRY_API_KEY%` prints key
- [ ] `git --version` prints version
- [ ] GitHub account exists
- [ ] `git config user.name` shows name
- [ ] `git config user.email` shows email
- [ ] `git remote -v` shows project URL
- [ ] `git branch` shows your branch with star