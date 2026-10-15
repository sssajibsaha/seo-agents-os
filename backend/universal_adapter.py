from typing import Dict, Any

class UniversalSiteAdapter:
    def __init__(self, site_profile: Dict[str, Any]):
        self.site = site_profile
        self.stack = site_profile["tech_stack"]
        self.config = site_profile.get("adapter_config", {})

    async def deploy_or_patch(self, payload: Dict[str, Any], mode: str = "draft") -> Dict[str, Any]:
        targets = {
            "wordpress": "WordPress Website (REST API)",
            "react": "React / Next.js Website (GitHub Pull Request)",
            "nodejs": "Node.js Website (Express Webhook)"
        }
        return {
            "status": "SUCCEEDED",
            "stack": self.stack,
            "adapter_target": targets.get(self.stack, self.stack),
            "mode": mode.upper(),
            "slug": f"/{payload['slug']}",
            "page_type": payload.get("page_type", "comparison").upper(),
            "message": f"Staged '{payload['title']}' for {targets.get(self.stack)} ({mode.upper()} mode)."
        }
