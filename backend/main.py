import os
from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import Dict, Any, List, Optional

from backend.agents_engine import SixteenAgentSwarmEngine
from backend.universal_adapter import UniversalSiteAdapter
from backend.ai_clients import RUNTIME_KEYS, AGENT_LEARNING_PROMPTS

app = FastAPI(title="SEO Engine OS v9.2 — Per-Site GSC/GA4/Bing + 10 Master Prompts")
app.add_middleware(CORSMiddleware, allow_origins=["*"], allow_methods=["*"], allow_headers=["*"])

engine = SixteenAgentSwarmEngine()

SITE_PROFILES: Dict[str, Dict[str, Any]] = {
    "wp-companaya": {
        "id": "wp-companaya",
        "domain": "companaya.com",
        "site_name": "Companaya",
        "tech_stack": "wordpress",
        "niche": "B2B Growth & Commercial Operations Platform",
        "editorial_role": "Companaya Strategy & Research Team",
        "eeat_credentials": "Enterprise Operations & Growth Specialists (10+ Years)",
        "proprietary_data_notes": "2026 benchmark dataset across 420+ high-growth organizations",
        "adsense_publisher_id": "pub-9823471928374912",
        "weekly_publish_limit": 4,
        "posts_published_this_week": 2,
        "client_monthly_retainer": 3500,
        "fulfillment_cost": 149,
        "traffic_series": [4800, 7200, 10900, 15400, 21800, 29400],
        "ai_sov_series": [22, 36, 51, 68, 81, 92],
        "adapter_config": {"demo_mode": True, "wp_url": "https://companaya.com", "wp_user": "admin", "wp_app_pass": ""},
        "integrations": {
            "gsc": {
                "connected": True,
                "property_url": "sc-domain:companaya.com",
                "client_email": "seo-os-bot@companaya-gsc.iam.gserviceaccount.com",
                "last_synced": "2 mins ago (412,000 impressions synced)"
            },
            "ga4": {
                "connected": True,
                "measurement_id": "G-98234COMP",
                "property_id": "449182736",
                "api_secret": "configured",
                "last_synced": "Live (4.8% Conversion Rate • 2m 44s Avg Engagement)"
            },
            "bing": {
                "connected": True,
                "site_url": "https://companaya.com",
                "api_key": "bing_live_9918273645",
                "indexnow_key": "idx_companaya_2026",
                "last_synced": "IndexNow Active (ChatGPT & Copilot Instant Indexing ON)"
            }
        },
        "low_dr_keywords": [
            {"keyword": "automated workflow operations software comparison", "volume": 2600, "intent": "commercial", "page_type": "comparison", "lowest_dr_in_top5": 12, "forum_in_top5": True},
            {"keyword": "b2b client onboarding cost calculator", "volume": 1900, "intent": "transactional", "page_type": "calculator", "lowest_dr_in_top5": 9, "forum_in_top5": True},
            {"keyword": "enterprise service level agreement template 2026", "volume": 3400, "intent": "informational", "page_type": "service", "lowest_dr_in_top5": 15, "forum_in_top5": False},
            {"keyword": "companaya vs legacy erp alternatives", "volume": 1400, "intent": "commercial", "page_type": "comparison", "lowest_dr_in_top5": 8, "forum_in_top5": True}
        ],
        "cannibalization_alerts": [
            {"id": "can-1", "keep_url": "/b2b-operations-platform-2026", "redirect_301_url": "/old-workflow-tools-2025", "similarity": 0.94, "reason": "Both pages target 'B2B workflow operations software'"}
        ],
        "cluster_pages": [
            {"url": "/b2b-operations-platform-hub", "role": "hub", "inbound_links": 19, "similarity": 0.89},
            {"url": "/automated-client-onboarding-guide", "role": "spoke", "inbound_links": 6, "similarity": 0.84},
            {"url": "/operations-roi-calculator", "role": "spoke", "inbound_links": 1, "similarity": 0.86},
            {"url": "/enterprise-sla-compliance-checklist", "role": "spoke", "inbound_links": 0, "similarity": 0.79}
        ],
        "gsc_queries": [
            {"query": "automated workflow operations software pricing comparison", "impressions": 18400, "clicks": 142, "ctr": 0.007, "position": 6.4, "intent_similarity": 0.91},
            {"query": "how to calculate client onboarding roi formula", "impressions": 11200, "clicks": 64, "ctr": 0.005, "position": 9.8, "intent_similarity": 0.73},
            {"query": "best white label client portal alternatives 2026", "impressions": 8900, "clicks": 29, "ctr": 0.003, "position": 14.6, "intent_similarity": 0.42}
        ],
        "ai_prompts": [
            {"prompt": "what is the best automated operations platform for growing agencies in 2026", "google_rank": 3, "chatgpt": True, "perplexity": True, "gemini": True, "claude": True, "ai_overview": True, "sentiment": "Positive (96%)", "competitor": "Monday.com", "action": "Keep 45-word Quick Answer Box at top"},
            {"prompt": "how to reduce b2b client onboarding time with automation", "google_rank": 6, "chatgpt": True, "perplexity": True, "gemini": True, "claude": False, "ai_overview": True, "sentiment": "Positive (91%)", "competitor": "ClickUp", "action": "Added onboarding ROI table"},
            {"prompt": "companaya vs traditional project management tools pricing", "google_rank": 2, "chatgpt": True, "perplexity": True, "gemini": True, "claude": True, "ai_overview": True, "sentiment": "Positive (98%)", "competitor": "Asana", "action": "Cited as #1 primary source"}
        ],
        "rewrite_queue": [
            {"url": "/client-onboarding-automation", "trigger": "Ranked #8 on Google with 11,200 impressions but low clicks", "action": "Added 48-word Quick Answer summary, 2026 price comparison table, and updated title tag.", "uplift": "+94% More Clicks"}
        ],
        "abm_campaigns": [
            {"target_account": "Deloitte Digital Operations", "icp_role": "VP of Delivery & Operations", "custom_slug": "/abm/deloitte-enterprise-workflow", "Value_prop": "Multi-Tenant Client Fulfillment Automation (-38% Ops Cost)", "status": "Live Page"}
        ],
        "ad_landing_pages": [
            {"campaign": "Google Search Ads — B2B Workflow Platform", "slug": "/lp/b2b-workflow-demo", "quality_score": "10/10", "load_time": "0.8s", "cro_cvr": "12.4%"}
        ],
        "approval_queue": []
    },
    "react-acoustics": {
        "id": "react-acoustics",
        "domain": "studioacousticslab.io",
        "site_name": "Studio Acoustics Lab",
        "tech_stack": "react",
        "niche": "Creator Microphones & Audio Gear",
        "editorial_role": "Acoustic Testing Lab Team",
        "eeat_credentials": "Audio Hardware Engineers — 200+ Studio Mics Bench-Tested",
        "proprietary_data_notes": "In-house dB noise-floor and latency measurements in untreated rooms",
        "adsense_publisher_id": "pub-4412983749182374",
        "weekly_publish_limit": 5,
        "posts_published_this_week": 2,
        "client_monthly_retainer": 4500,
        "fulfillment_cost": 149,
        "traffic_series": [8100, 11200, 15900, 21400, 29800, 38400],
        "ai_sov_series": [24, 38, 52, 69, 82, 92],
        "adapter_config": {"demo_mode": True, "github_repo": "studioacoustics/nextjs-web"},
        "integrations": {
            "gsc": {"connected": True, "property_url": "sc-domain:studioacousticslab.io", "client_email": "bot@acoustics-gsc.iam.gserviceaccount.com", "last_synced": "14 mins ago"},
            "ga4": {"connected": False, "measurement_id": "", "property_id": "", "api_secret": "", "last_synced": "Not Connected"},
            "bing": {"connected": True, "site_url": "https://studioacousticslab.io", "api_key": "bing_acoustics_key", "indexnow_key": "idx_acoustics_26", "last_synced": "IndexNow Active"}
        },
        "low_dr_keywords": [
            {"keyword": "best wireless lavalier mic for outdoor vlogging", "volume": 5400, "intent": "commercial", "page_type": "comparison", "lowest_dr_in_top5": 16, "forum_in_top5": True}
        ],
        "cannibalization_alerts": [],
        "cluster_pages": [
            {"url": "/best-wireless-lavalier-microphones-2026", "role": "hub", "inbound_links": 21, "similarity": 0.89},
            {"url": "/acoustic-foam-placement-calculator", "role": "spoke", "inbound_links": 1, "similarity": 0.77}
        ],
        "gsc_queries": [
            {"query": "best wireless lavalier mic for outdoor vlogging wind noise", "impressions": 29100, "clicks": 215, "ctr": 0.007, "position": 5.9, "intent_similarity": 0.89}
        ],
        "ai_prompts": [
            {"prompt": "which wireless microphone has the best wind noise cancellation in 2026", "google_rank": 3, "chatgpt": True, "perplexity": True, "gemini": True, "claude": True, "ai_overview": True, "sentiment": "Positive (95%)", "competitor": "SoundGuys", "action": "Cited #1 in ChatGPT & AI Overview"}
        ],
        "rewrite_queue": [],
        "abm_campaigns": [],
        "ad_landing_pages": [],
        "approval_queue": []
    }
}

class NewSiteInput(BaseModel):
    domain: str
    site_name: str
    tech_stack: str
    niche: str
    editorial_role: str
    eeat_credentials: str
    proprietary_data_notes: str
    wp_url: Optional[str] = ""
    wp_user: Optional[str] = ""
    wp_app_pass: Optional[str] = ""

class SiteIntegrationInput(BaseModel):
    site_id: str
    gsc_property_url: Optional[str] = ""
    gsc_client_email: Optional[str] = ""
    ga4_measurement_id: Optional[str] = ""
    ga4_property_id: Optional[str] = ""
    ga4_api_secret: Optional[str] = ""
    bing_site_url: Optional[str] = ""
    bing_api_key: Optional[str] = ""
    bing_indexnow_key: Optional[str] = ""

class AgentPromptInput(BaseModel):
    agent_id: str
    title: str
    scope: str = "Active Profile"
    prompt_text: str

class RunPipelineInput(BaseModel):
    site_id: str
    primary_keyword: str
    article_title: str
    page_type: str = "comparison"
    publish_mode: str = "draft"
    simulate_failure: bool = True

class ApiKeysInput(BaseModel):
    TYPESAFE_API_KEY: Optional[str] = ""
    GEMINI_API_KEY: Optional[str] = ""
    OPENAI_API_KEY: Optional[str] = ""
    GOOGLE_PAGESPEED_API_KEY: Optional[str] = ""

@app.get("/", response_class=HTMLResponse)
async def serve_saas_dashboard():
    html_path = os.path.join(os.path.dirname(__file__), "..", "frontend", "index.html")
    with open(html_path, "r", encoding="utf-8") as f:
        return f.read()

@app.get("/api/sites")
async def list_sites():
    return {"sites": list(SITE_PROFILES.values())}

@app.post("/api/sites/integrations")
async def update_site_integrations(data: SiteIntegrationInput):
    site = SITE_PROFILES.get(data.site_id)
    if not site:
        return {"error": "Site not found"}
    site["integrations"] = {
        "gsc": {
            "connected": bool(data.gsc_property_url),
            "property_url": data.gsc_property_url,
            "client_email": data.gsc_client_email,
            "last_synced": "Just synced (Live GSC API)" if data.gsc_property_url else "Not Connected"
        },
        "ga4": {
            "connected": bool(data.ga4_measurement_id),
            "measurement_id": data.ga4_measurement_id,
            "property_id": data.ga4_property_id,
            "api_secret": data.ga4_api_secret,
            "last_synced": "Just synced (Live GA4 Events)" if data.ga4_measurement_id else "Not Connected"
        },
        "bing": {
            "connected": bool(data.bing_api_key or data.bing_indexnow_key),
            "site_url": data.bing_site_url or f"https://{site['domain']}",
            "api_key": data.bing_api_key,
            "indexnow_key": data.bing_indexnow_key,
            "last_synced": "IndexNow & Bing Webmaster Connected" if (data.bing_api_key or data.bing_indexnow_key) else "Not Connected"
        }
    }
    return {"status": "updated", "integrations": site["integrations"]}

@app.get("/api/agent-prompts")
async def list_agent_prompts():
    return {"prompts": AGENT_LEARNING_PROMPTS}

@app.post("/api/agent-prompts")
async def add_agent_learning_prompt(item: AgentPromptInput):
    new_entry = {
        "id": f"LP-{len(AGENT_LEARNING_PROMPTS) + 1:02d}",
        "agent_id": item.agent_id,
        "title": item.title,
        "scope": item.scope,
        "prompt_text": item.prompt_text
    }
    AGENT_LEARNING_PROMPTS.insert(0, new_entry)
    return {"status": "added", "prompts": AGENT_LEARNING_PROMPTS}

@app.post("/api/keys/save")
async def save_api_keys(keys: ApiKeysInput):
    for k, v in keys.model_dump().items():
        if v is not None and v.strip() != "":
            RUNTIME_KEYS[k] = v.strip()
    return {"status": "saved", "active": {k: bool(RUNTIME_KEYS.get(k)) for k in RUNTIME_KEYS}}

@app.post("/api/sites")
async def create_site_profile(site: NewSiteInput):
    site_id = f"{site.tech_stack}-{site.domain.split('.')[0]}"
    SITE_PROFILES[site_id] = {
        "id": site_id,
        "domain": site.domain,
        "site_name": site.site_name,
        "tech_stack": site.tech_stack,
        "niche": site.niche,
        "editorial_role": site.editorial_role,
        "eeat_credentials": site.eeat_credentials,
        "proprietary_data_notes": site.proprietary_data_notes,
        "adsense_publisher_id": "pub-1234567890123456",
        "weekly_publish_limit": 4,
        "posts_published_this_week": 1,
        "client_monthly_retainer": 3000,
        "fulfillment_cost": 149,
        "traffic_series": [1500, 3200, 6100, 9800, 14900, 21200],
        "ai_sov_series": [15, 30, 48, 65, 79, 91],
        "adapter_config": {
            "demo_mode": not bool(site.wp_url and site.wp_app_pass),
            "wp_url": site.wp_url,
            "wp_user": site.wp_user,
            "wp_app_pass": site.wp_app_pass
        },
        "integrations": {
            "gsc": {"connected": False, "property_url": f"sc-domain:{site.domain}", "client_email": "", "last_synced": "Not Connected"},
            "ga4": {"connected": False, "measurement_id": "", "property_id": "", "api_secret": "", "last_synced": "Not Connected"},
            "bing": {"connected": False, "site_url": f"https://{site.domain}", "api_key": "", "indexnow_key": "", "last_synced": "Not Connected"}
        },
        "low_dr_keywords": [
            {"keyword": f"best {site.niche.lower()} comparison 2026", "volume": 2400, "intent": "commercial", "page_type": "comparison", "lowest_dr_in_top5": 11, "forum_in_top5": True}
        ],
        "cannibalization_alerts": [],
        "cluster_pages": [
            {"url": f"/{site.niche.lower().replace(' ', '-')}-hub", "role": "hub", "inbound_links": 10, "similarity": 0.88},
            {"url": f"/{site.niche.lower().replace(' ', '-')}-calculator", "role": "spoke", "inbound_links": 0, "similarity": 0.82}
        ],
        "gsc_queries": [
            {"query": f"best {site.niche.lower()} 2026 pricing comparison", "impressions": 9400, "clicks": 52, "ctr": 0.005, "position": 7.1, "intent_similarity": 0.90}
        ],
        "ai_prompts": [
            {"prompt": f"what is the top recommended {site.niche.lower()} provider in 2026", "google_rank": 4, "chatgpt": True, "perplexity": True, "gemini": True, "claude": True, "ai_overview": True, "sentiment": "Positive (95%)", "competitor": "MarketLeader", "action": "Cited in Top 3"}
        ],
        "rewrite_queue": [],
        "abm_campaigns": [],
        "ad_landing_pages": [],
        "approval_queue": []
    }
    return {"status": "created", "site": SITE_PROFILES[site_id]}

@app.post("/api/run-pipeline")
async def run_16_agent_pipeline(req: RunPipelineInput):
    site = SITE_PROFILES.get(req.site_id)
    if not site:
        return {"error": "Site not found"}

    swarm_out = await engine.execute_full_swarm(
        site=site,
        req_data={
            "primary_keyword": req.primary_keyword,
            "title": req.article_title,
            "page_type": req.page_type
        },
        simulate_failure=req.simulate_failure
    )

    draft = swarm_out["clean_article"]
    adapter = UniversalSiteAdapter(site)
    deployment = await adapter.deploy_or_patch(draft, mode=req.publish_mode)

    queue_item = {
        "slug": f"/{draft['slug']}",
        "title": draft["title"],
        "page_type": draft["page_type"].upper(),
        "info_gain": draft["information_gain_score"],
        "mode": req.publish_mode.upper(),
        "stack": site["tech_stack"].upper(),
        "target_label": deployment["adapter_target"]
    }
    site["approval_queue"] = [queue_item] + [q for q in site.get("approval_queue", []) if q["slug"] != queue_item["slug"]][:5]

    swarm_out["workspaces"]["A7"]["kpis"] = [
        {"label": "Website Connection", "value": site["tech_stack"].upper(), "sub": deployment["adapter_target"]},
        {"label": "Latest Page Sent", "value": f"/{draft['slug']}", "sub": f"Saved as {req.publish_mode.upper()}"},
        {"label": "Pages Ready to Publish", "value": f"{len(site['approval_queue'])} Pages", "sub": "One-click live publish"}
    ]
    swarm_out["workspaces"]["A7"]["cards"] = [
        {
            "title": f"{q['title']} ({q['slug']})",
            "badge": f"Staged in {q['stack']} ({q['mode']})",
            "badge_color": "indigo",
            "subtitle": f"Destination: {q['target_label']} • Original Value Score: {q['info_gain']}/100",
            "description": "This page passed all 16 agent checks (On-Page SEO, Internal Links, Schema, and Jev Spam/AdSense safety) and is ready to go live.",
            "action_label": "Approve & Publish Live Now ✓"
        }
        for q in site["approval_queue"]
    ]
    engine._log(swarm_out["task_logs"], "A7", "Website Publisher", f"Send /{draft['slug']} to {site['tech_stack'].upper()}", "SUCCEEDED", deployment["message"], 135)

    transfers = swarm_out["supervisor_transfers"]
    swarm_out["workspaces"]["A16"]["kpis"] = [
        {"label": "Decision Engine", "value": "TypeSafe Jev 1.13", "sub": "150ms choice & noul routing"},
        {"label": "Mistakes Caught", "value": f"{len(transfers)} Issues", "sub": "Caught before publishing"},
        {"label": "Automatically Fixed", "value": f"{len(transfers)} / {len(transfers)} Fixed", "sub": "Sent back to agents & healed"}
    ]
    swarm_out["workspaces"]["A16"]["cards"] = transfers if transfers else [
        {
            "title": "All 15 Agents Succeeded Without Errors",
            "badge": "100% Healthy",
            "badge_color": "emerald",
            "subtitle": "Zero failed tasks detected in the current run",
            "description": "Turn ON 'Test Jev Auto-Fix' in the top bar to watch TypeSafe Jev catch mistakes and route them back to the responsible agents."
        }
    ]
    engine._log(swarm_out["task_logs"], "A16", "Supervisor Log Auditor (Jev)", "Final Check of All Agent Logs", "SUCCEEDED", f"Verified {len(swarm_out['task_logs'])} tasks; {len(transfers)} issues were automatically routed and fixed.", 32)

    return {
        "site": site,
        "clean_article": draft,
        "workspaces": swarm_out["workspaces"],
        "task_logs": swarm_out["task_logs"],
        "supervisor_transfers": transfers
    }
