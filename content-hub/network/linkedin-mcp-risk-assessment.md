# LinkedIn MCP Risk Assessment and Decision

**Decision date:** 2026-08-05  
**Decision:** Do not install or connect an unofficial LinkedIn browser/scraping MCP.  
**Approved pattern:** Local, human-approved professional networking assistant.

## Decision summary

Connecting a local MCP to the user's own LinkedIn account would not remove the
platform risk. The relevant risk is the method of access and the automated activity,
not only who owns the account. LinkedIn's current User Agreement prohibits software,
scripts, browser plugins, and other processes used to scrape or copy its services,
and prohibits bots or other unauthorized automated methods that add contacts, send
messages, or create, comment on, like, share, or re-share posts.

The project therefore keeps LinkedIn outside the automation boundary. The repository
can prepare drafts and track confirmed outcomes, but the user must open LinkedIn,
verify the recipient or post, and manually perform each send or publish action.

## Evidence reviewed

| Source | What it establishes | Implication |
|---|---|---|
| [LinkedIn User Agreement](https://www.linkedin.com/legal/user-agreement) | Section 8.2 prohibits scraping/copying and unauthorized automated access or engagement | Browser-driving or scraping MCP is not an acceptable default |
| [LinkedIn Automated Activity help](https://www.linkedin.com/help/linkedin/answer/a1340567/automated-activity-on-linkedin?lang=en) | LinkedIn says third-party software or extensions that scrape or automate activity violate the User Agreement and can lead to restriction | Account ownership does not make an unofficial automation tool safe |
| [LinkedIn Prohibited Software help](https://www.linkedin.com/help/linkedin/answer/a1341387/prohibited-software-and-extensions?lang=en) | Crawlers, bots, browser plug-ins, and extensions that scrape or automate activity are not permitted | Do not install a community LinkedIn scraper/extension for this workflow |
| [Share on LinkedIn API](https://learn.microsoft.com/en-us/linkedin/consumer/integrations/self-serve/share-on-linkedin) | A documented API can create shares for an approved application and permission | This is a scoped publishing integration, not general member outreach/search |
| [Sign In with LinkedIn](https://learn.microsoft.com/en-us/linkedin/consumer/integrations/self-serve/sign-in-with-linkedin) | A documented OAuth identity integration exists | OAuth is not permission to scrape the website or automate unrelated actions |
| [LinkedIn Job Posting API](https://learn.microsoft.com/en-us/linkedin/talent/job-postings/api/create-jobs?view=li-lts-2026-03) | The documented jobs API creates, updates, renews, and closes job postings | It is designed for job posters/ATS workflows, not ordinary member job search or auto-apply |
| [OpenAI Apps and MCP guidance](https://help.openai.com/en/articles/12584461-developer-mode-and-full-mcp-connectors-in-chatgpt-beta) | Custom MCP apps require review; the owner is responsible for verifying third-party apps and connectors | Any future MCP must be scoped, reviewed, and tested before use |

## Risk matrix

| Proposed capability | Risk | Decision |
|---|---|---|
| Read LinkedIn pages through a logged-in browser | Scraping/unauthorized access; credentials or cookies may be exposed | Reject |
| Search members or jobs through an unofficial scraper | Terms, privacy, data provenance, and account-restriction risk | Reject |
| Auto-send connection requests or messages | Inauthentic engagement and irreversible external action | Reject |
| Auto-like, comment, repost, or publish | Automated engagement and reputational risk | Reject |
| Store LinkedIn cookies, passwords, or session tokens | Credential theft and account takeover risk | Reject |
| User supplies a profile URL, screenshot, or copied text for analysis | Limited, user-directed input; still requires privacy and accuracy review | Allow |
| Local draft generation and contact tracking | No platform access; user remains the sender | Allow |
| Official OAuth/API integration with narrowly approved scope | Potentially allowable only under the relevant LinkedIn product terms and permissions | Reassess only with written scope and approval |

## Approved local tool boundary

The files in this folder may:

- analyse user-supplied profile text, screenshots, or exports;
- use repository-owned portfolio evidence to propose profile improvements;
- prepare posts, comments, connection notes, and follow-ups for review;
- track contacts, manual actions, dates, permissions, and outcomes;
- promote a contact into the commercial tracker only after identifiable interest.

They may not:

- log in to LinkedIn or request a LinkedIn password, cookie, or session token;
- scrape, crawl, mirror, or extract LinkedIn pages or member data;
- send, publish, like, comment, connect, apply, or otherwise act on LinkedIn;
- infer private intent from a profile view, recommendation, or public listing;
- treat a generated draft or researched target as a sent action or qualified lead.

## Reconsideration gate

Do not revisit the “no unofficial LinkedIn MCP” decision unless all of the following
are available and documented:

1. A first-party or explicitly authorised LinkedIn product scope that covers the
   intended operation.
2. OAuth or another approved authentication flow; never browser cookies or passwords.
3. A written tool inventory, data-retention policy, privacy policy, and owner.
4. Read-only mode by default and explicit confirmation for every external write.
5. A kill switch, audit log, rate limits, error handling, and a tested rollback path.
6. Confirmation that the intended use complies with the then-current LinkedIn terms
   and the applicable privacy/anti-spam requirements.

Until this gate is met, the local human-approved workflow is the complete approved
implementation for this project.
