# 🛡️ AI Security Journey

I'm a cybersecurity student working in security operations, documenting my path into **AI security** — every lesson, lab, and project, built only with free tools.

---

## 👋 About me

- **Cybersecurity BBA student** at Baruch College (expected December 2027)
- **College Aide, NYC Office of Technology and Innovation** — Resilience Operations / IRT team
- Hands-on with proxy, firewall, DNS, and security operations tooling: IBM QRadar, Palo Alto Panorama, Symantec Management Center, Infoblox
- **Goal:** an AI security engineering role after graduation

## 🎯 Why this repo

Companies are shipping AI chatbots and agents faster than they can secure them. AI security engineers do four things: understand the code being written, map the AI attack surface, use AI to defend, and test AI like an attacker. This repo tracks how I'm building those skills, step by step.

---

## 🗺️ Roadmap

| # | Lesson | Status |
| --- | --- | --- |
| 1 | How AI apps get hacked (OWASP Top 10 for LLMs) | ✅ Done |
| 2 | Git, GitHub & CI/CD pipelines (GitHub Actions) |✅ Done |
| 3 | Containers (Docker) | ✅ Done |
| 4 | Security scanners in the pipeline | ⬜ |
| 5 | Cloud (AWS) | ⬜ |
| 6 | Infrastructure as Code (Terraform) | ⬜ |
| 7 | Kubernetes & ECS | ⬜ |
| 8 | Data platform security (Databricks / Snowflake) | ⬜ |
| 9 | GRC & the EU AI Act | ⬜ |
| 10 | Building AI agents (n8n) | ⬜ |
| 11 | Mapping the AI attack surface | ⬜ |
| 12 | Attacking AI (threat modeling & red teaming) | ⬜ |
| 13 | Defending AI (guardrails & limited agents) | ⬜ |

---

## 📓 Lesson log

### Lesson 1 — OWASP Top 10 for LLM Applications ✅

**What it is:** OWASP's ranked list of the most common ways AI apps get attacked — the shared vocabulary of AI security.

| ID | Risk | In one line |
| --- | --- | --- |
| LLM01 | Prompt Injection | Words that trick the AI into ignoring its rules (typed directly or hidden in content it reads) |
| LLM02 | Sensitive Information Disclosure | The AI leaks private data |
| LLM03 | Supply Chain | A model, dataset, or library you depend on is malicious or vulnerable |
| LLM04 | Data and Model Poisoning | Bad data corrupts what the AI learns |
| LLM05 | Improper Output Handling | The app trusts and runs AI output without checking it |
| LLM06 | Excessive Agency | The AI has more tools, permissions, or freedom than it needs |
| LLM07 | System Prompt Leakage | The AI reveals its hidden instructions (and any secrets in them) |
| LLM08 | Vector and Embedding Weaknesses | Flaws in the document library the AI looks things up in (RAG) |
| LLM09 | Misinformation | The AI confidently makes things up and people act on it |
| LLM10 | Unbounded Consumption | Runaway usage crashes the app or runs up the bill |

**My memory trick:** Trick, Leak, Parts, Poison, Trust, Power, Secrets, Library, Lies, Bill.

**Hands-on:**
- [Gandalf by Lakera](https://gandalf.lakera.ai/) — in progress
- [PortSwigger Web LLM attacks labs](https://portswigger.net/web-security/llm-attacks)

**Key takeaway:** An LLM can't reliably tell instructions from data, so you have to assume it can be tricked — and limit what a tricked AI can reach.

### Lesson 2 — Git, GitHub & CI/CD 🟡

**What it is:** A CI/CD pipeline automatically checks every code change (CI) and ships it to production if it passes (CD). It's the best place to add security checks before anything reaches customers.

**Learned so far:** repos, commits, branches, pull requests, workflows → jobs → steps, runners, GitHub Secrets, secret scanning vs. push protection, Dependabot vs. CodeQL, branch protection, and why pipelines themselves are targets (Codecov 2021, tj-actions 2025).

**Next:** build my first GitHub Actions workflow in this repo.

---

## 🧪 Labs & CTFs

### Lakera Agent Breaker

| Challenge | OWASP risk | Status | What I learned |
| --- | --- | --- | --- |
| Cycling Coach — extract the system prompt | LLM07 | 🟡 In progress | Defenses watch for trigger phrases like "original instructions"; indirect, on-topic asks get further |
| Thingularity — extract the agent's tools | LLM07 / LLM06 | ⬜ | |
| Solace AI — jailbreak a support bot | LLM01 | ⬜ | |
| Trippy Planner — indirect injection via a website | LLM01 / LLM05 | ⬜ | |
| Clause AI — exfiltrate protected data | LLM02 | ⬜ | |

---

## 🚧 Projects (coming soon)

1. **Secure AI App Pipeline** — an AI chatbot wrapped in a GitHub Actions DevSecOps pipeline: secret, code, dependency, container, and Terraform scanning, plus automated AI red-teaming before every deploy.
2. **AI SOC Triage Agent** — an n8n agent that triages security alerts, then gets attacked, defended with guardrails and least privilege, and mapped to the EU AI Act and NIST AI RMF.

## 🧰 Tools (all free)

GitHub Actions · Docker · Ollama · Gemini API (free tier) · Gitleaks · Semgrep · Trivy · Checkov · Terraform · kind · n8n · garak · promptfoo · LLM Guard · CISO Assistant · Databricks Free Edition

---

## 🤝 Connect

[LinkedIn](https://www.linkedin.com/in/joseph-commisso-846351257/) — always happy to talk AI security, SOC work, or DevSecOps.
