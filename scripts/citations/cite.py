"""Render docs templates: {{key}} -> <sup>[Source](url#:~:text=exact quote)</sup>.

Every quote below was checked verbatim against the live page text on 2026-11-12.
"""
import re, sys, pathlib
from urllib.parse import quote

SRC = {
    "bloom": ("Bloomberry", "https://bloomberry.com/blog/i-analyzed-1000-forward-deployed-engineer-jobs-what-i-learned/"),
    "rfs": ("Recruiting from Scratch", "https://www.recruitingfromscratch.com/blog/forward-deployed-engineer-salary-in-2026-real-data-from-1-9-million-job-postings"),
    "parahire": ("Paraform", "https://www.paraform.com/insights/how-to-hire-a-forward-deployed-engineer"),
    "para": ("Paraform", "https://www.paraform.com/insights/forward-deployed-ai-engineer"),
    "fortune": ("Fortune", "https://fortune.com/2026/09/03/forward-deployed-engineers-fast-growing-six-figure-silicon-valley-job-integrate-ai-with-customers-tech-careers-palantir/"),
    "techscoop": ("TechScoop", "https://techscoop.substack.com/p/why-forward-deployed-engineers-are"),
    "ik": ("Interview Kickstart", "https://interviewkickstart.com/blogs/articles/forward-deployed-engineer-skills-job-posting-analysis"),
    "masai": ("Masai School", "https://www.masaischool.com/blog/forward-deployed-engineer-skills/"),
    "persp": ("Perspective AI", "https://getperspective.ai/blog/forward-deployed-engineer-vs-ml-engineer-vs-solutions-architect-2026/markdown"),
    "simpl": ("Simpliaxis", "https://www.simpliaxis.com/resources/roles-confused-with-fde"),
    "raydar": ("Raydar posting", "https://apply.workable.com/raydar/jobs/view/57688ECE6B.md"),
}

QUOTES = {
    "b_median": ("bloom", "the median comes in at $173,816"),
    "b_equity": ("bloom", "70% of FDE jobs mention equity"),
    "b_quota": ("bloom", "0% are quota-carrying"),
    "b_python": ("bloom", "Python dominates at 66%"),
    "b_agents": ("bloom", "AI Agents (35%)"),
    "b_ts": ("bloom", "TypeScript shows up in 35%"),
    "b_cloud": ("bloom", "AWS (32%)"),
    "b_llm": ("bloom", "LLM experience (31%)"),
    "b_three": ("bloom", "three different jobs"),
    "r_median": ("rfs", "median salary for a Forward Deployed Engineer is $195,000"),
    "r_sf": ("rfs", "8% higher than the median remote"),
    "ph_mid": ("parahire", "with a midpoint of $183,000"),
    "ph_loop": ("parahire", "Decomposition or case study"),
    "pa_hire": ("para", "Anthropic, OpenAI, Scale AI, Palantir, and Salesforce are all actively hiring"),
    "pa_startups": ("para", "Glean, Cresta, Hippocratic AI, Sierra, Decagon"),
    "pa_anth": ("para", "Anthropic has scaled its Applied AI team aggressively"),
    "pa_travel": ("para", "expect 40-60% travel"),
    "f_big": ("fortune", "OpenAI and Anthropic currently all have openings"),
    "f_pal": ("fortune", "Palantir has long been known for its forward-deployed model"),
    "t_42": ("techscoop", "forward deployed engineering roles grew 42-fold between 2023 and 2025"),
    "t_titles": ("techscoop", "applied AI engineer, deployment engineer, field engineer and solutions engineer"),
    "ik_req": ("ik", "the most common requirements included production coding"),
    "ik_proj": ("ik", "A strong project could include an evaluation dataset"),
    "m_evals": ("masai", "Evals, meaning systematic tests"),
    "m_int": ("masai", "The common thread is integration work"),
    "m_disc": ("masai", "discovery and technical scoping"),
    "m_adopt": ("masai", "production adoption and eval-driven feedback"),
    "p_se": ("persp", "A solutions engineer is pre-sales-aligned"),
    "p_sa": ("persp", "Solutions architect in depth: ships contracts, not code"),
    "s_after": ("simpl", "one centred on building and delivering after the sale is genuine forward deployed work"),
    "s_cousins": ("simpl", "Implementation consultant and professional services engineer: the closest cousins"),
    "s_cse": ("simpl", "Customer success engineer and technical account manager: support rather than build"),
    "ry_pay": ("raydar", "Base salary: USD 230,000 to 300,000 per year"),
}


def frag(text):
    return quote(text, safe="").replace("-", "%2D")


def link(key):
    src, text = QUOTES[key]
    name, url = SRC[src]
    return f"{url}#:~:text={frag(text)}", name, text


def render(s):
    def sub(m):
        url, name, _ = link(m.group(1))
        return f'<sup>[{name}]({url})</sup>'
    return re.sub(r"\{\{(\w+)\}\}", sub, s)


if __name__ == "__main__":
    tpl_dir, out_dir = map(pathlib.Path, sys.argv[1:3])
    for tpl in tpl_dir.rglob("*.md"):
        out = out_dir / tpl.relative_to(tpl_dir)
        out.write_text(render(tpl.read_text()))
        print("rendered", out)
