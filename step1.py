from dataclasses import dataclass, field
from typing import List
import json
 
 
# ─────────────────────────────────────────
# 1. Data Models
# ─────────────────────────────────────────
 
@dataclass
class BrandDetails:
    name: str
    niche: str
    tone: List[str]  # eg: ["Fun & Casual", "Inspirational"]
 
 
@dataclass
class TargetAudience:
    age_group: str        # eg: "25-35"
    location: str         # eg: "Hyderabad, India"
    interests: List[str]  # eg: ["healthy food", "fitness"]
    pain_points: List[str]  # eg: ["no time to cook", "budget tight"]
    platforms: List[str]  # eg: ["Instagram", "YouTube"]
 
 
@dataclass
class ContentGoals:
    primary_goals: List[str]  # eg: ["Brand Awareness", "Drive Sales"]
 
 
@dataclass
class ProblemInput:
    brand: BrandDetails
    audience: TargetAudience
    goals: ContentGoals
 
 
# ─────────────────────────────────────────
# 2. Input Collector
# ─────────────────────────────────────────
 
class ProblemInputCollector:
    """
    User nunchi brand, audience, goals collect chesi
    validate chestuundi.
    """
 
    VALID_TONES = [
        "Fun & Casual", "Professional", "Inspirational",
        "Educational", "Bold & Direct", "Minimal & Clean"
    ]
 
    VALID_PLATFORMS = [
        "Instagram", "YouTube", "LinkedIn",
        "Twitter/X", "Blog/SEO", "WhatsApp"
    ]
 
    VALID_GOALS = [
        "Brand Awareness", "Drive Sales", "Community Building",
        "Website Traffic", "Lead Generation", "Follower Growth"
    ]
 
    def collect(self) -> ProblemInput:
        print("\n" + "="*50)
        print("  CONTENT STRATEGY AGENT — STEP 1: INPUT")
        print("="*50)
 
        brand = self._collect_brand()
        audience = self._collect_audience()
        goals = self._collect_goals()
 
        return ProblemInput(brand=brand, audience=audience, goals=goals)
 
    # ── Brand ──
    def _collect_brand(self) -> BrandDetails:
        print("\n[ BRAND DETAILS ]")
 
        name = input("Brand name: ").strip()
        if not name:
            raise ValueError("Brand name empty ga undakudadu.")
 
        niche = input("Niche/Industry (eg: Food, Tech, Fashion): ").strip()
        if not niche:
            raise ValueError("Niche empty ga undakudadu.")
 
        print(f"Tone options: {', '.join(self.VALID_TONES)}")
        tone_input = input("Brand tone select cheyyandi (comma separated): ")
        tones = [t.strip() for t in tone_input.split(",") if t.strip()]
        invalid = [t for t in tones if t not in self.VALID_TONES]
        if invalid:
            print(f"Warning: Invalid tones ignored → {invalid}")
        tones = [t for t in tones if t in self.VALID_TONES]
        if not tones:
            tones = ["Professional"]  # default
 
        return BrandDetails(name=name, niche=niche, tone=tones)
 
    # ── Audience ──
    def _collect_audience(self) -> TargetAudience:
        print("\n[ TARGET AUDIENCE ]")
 
        age_group = input("Age group (eg: 18-25, 25-35): ").strip() or "25-35"
        location = input("Location/Market (eg: Hyderabad, India): ").strip() or "India"
 
        interests_input = input("Audience interests (comma separated): ")
        interests = [i.strip() for i in interests_input.split(",") if i.strip()]
 
        pain_points_input = input("Pain points (comma separated): ")
        pain_points = [p.strip() for p in pain_points_input.split(",") if p.strip()]
 
        print(f"Platform options: {', '.join(self.VALID_PLATFORMS)}")
        plat_input = input("Platforms select cheyyandi (comma separated): ")
        platforms = [p.strip() for p in plat_input.split(",") if p.strip()]
        platforms = [p for p in platforms if p in self.VALID_PLATFORMS]
        if not platforms:
            platforms = ["Instagram"]  # default
            return TargetAudience(
            age_group=age_group,
            location=location,
            interests=interests,
            pain_points=pain_points,
            platforms=platforms
        )
 
    # ── Goals ──
    def _collect_goals(self) -> ContentGoals:
        print("\n[ CONTENT GOALS ]")
        print(f"Goal options: {', '.join(self.VALID_GOALS)}")
 
        goals_input = input("Goals select cheyyandi (comma separated): ")
        goals = [g.strip() for g in goals_input.split(",") if g.strip()]
        goals = [g for g in goals if g in self.VALID_GOALS]
        if not goals:
            goals = ["Brand Awareness"]  # default
 
        return ContentGoals(primary_goals=goals)
 
 
# ─────────────────────────────────────────
# 3. Validator
# ─────────────────────────────────────────
 
class InputValidator:
    """Collected input ni validate chestuundi."""
 
    def validate(self, problem: ProblemInput) -> bool:
        errors = []
 
        if not problem.brand.name:
            errors.append("Brand name missing.")
        if not problem.brand.niche:
            errors.append("Niche missing.")
        if not problem.audience.platforms:
            errors.append("Platforms missing.")
        if not problem.goals.primary_goals:
            errors.append("Goals missing.")
 
        if errors:
            print("\n[VALIDATION ERRORS]")
            for e in errors:
                print(f"  ✗ {e}")
            return False
 
        print("\n✓ Input valid — Step 2 ki pass cheyyadam ready!")
        return True
 
 
# ─────────────────────────────────────────
# 4. JSON Exporter
# ─────────────────────────────────────────
 
class InputExporter:
    """ProblemInput ni JSON ga export chestuundi — next agent ki pass avutundi."""
 
    def to_dict(self, problem: ProblemInput) -> dict:
        return {
            "step": 1,
            "brand": {
                "name": problem.brand.name,
                "niche": problem.brand.niche,
                "tone": problem.brand.tone
            },
            "target_audience": {
                "age_group": problem.audience.age_group,
                "location": problem.audience.location,
                "interests": problem.audience.interests,
                "pain_points": problem.audience.pain_points,
                "platforms": problem.audience.platforms
            },
            "content_goals": problem.goals.primary_goals
        }
 
    def save(self, problem: ProblemInput, filepath: str = "step1_output.json"):
        data = self.to_dict(problem)
        with open(filepath, "w", encoding="utf-8") as f:
            json.dump(data, f, indent=2, ensure_ascii=False)
        print(f"\n✓ JSON saved → {filepath}")
        return data
 
 
# ─────────────────────────────────────────
# 5. Main Runner
# ─────────────────────────────────────────
 
def run_step1() -> dict:
    collector = ProblemInputCollector()
    validator = InputValidator()
    exporter = InputExporter()
 
    # Collect
    problem = collector.collect()
 
    # Validate
    if not validator.validate(problem):
        raise SystemExit("Invalid input. Please retry.")
 
    # Export → Step 2 ki pass
    payload = exporter.save(problem)
 
    print("\n[ STEP 1 OUTPUT PREVIEW ]")
    print(json.dumps(payload, indent=2, ensure_ascii=False))
 
    return payload  # Step 2 (Research Agent) ki return
 
 
# ─────────────────────────────────────────
# 6. Demo Mode (hardcoded example)
# ─────────────────────────────────────────
 
def run_demo() -> dict:
    """Terminal input lekundane demo run cheyyataniki."""
    problem = ProblemInput(
        brand=BrandDetails(
            name="FitBite",
            niche="Healthy Snacks",
            tone=["Fun & Casual", "Inspirational"]
        ),
        audience=TargetAudience(
            age_group="22-35",
            location="Hyderabad, India",
            interests=["fitness", "healthy eating", "quick recipes"],
            pain_points=["no time to cook", "junk food temptation", "budget tight"],
            platforms=["Instagram", "YouTube"]
        ),
        goals=ContentGoals(
            primary_goals=["Brand Awareness", "Follower Growth", "Drive Sales"]
        )
    )
 
    validator = InputValidator()
    exporter = InputExporter()
 
    validator.validate(problem)
    payload = exporter.save(problem, "step1_output.json")
 
    print("\n[ STEP 1 DEMO OUTPUT ]")
    print(json.dumps(payload, indent=2, ensure_ascii=False))
 
    return payload
 
 
if __name__ == "__main__":
    # Demo run cheyyataniki:
    run_demo()
 
    # Real input kavali ante:
    # run_step1()
 

 
