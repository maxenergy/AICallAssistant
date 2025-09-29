import random
from typing import Dict, Any, List

# In a real application, this would be stored in a database or a configuration file.
experiments: Dict[str, List[Dict[str, Any]]] = {
    "opening_line_test": [
        {
            "variant": "A",
            "script_part": {
                "opening": "您好，请问是 {company_name} 的决策人吗？我们注意到贵公司最近在[相关领域]有新的动态。"
            }
        },
        {
            "variant": "B",
            "script_part": {
                "opening": "您好，我是[您的名字]，来自[您的公司]。我们专注于帮助像 {company_name} 这样的企业在[具体领域]提升效率。"
            }
        }
    ]
}

def get_script_variant(experiment_name: str, company_name: str) -> Dict[str, Any]:
    """
    Selects a script variant for a given experiment.

    This simple implementation uses random selection.
    """
    if experiment_name not in experiments:
        raise ValueError(f"Experiment '{experiment_name}' not found.")

    selected_variant = random.choice(experiments[experiment_name])

    # Personalize the script part
    script_part = selected_variant["script_part"]
    for key, value in script_part.items():
        if isinstance(value, str):
            script_part[key] = value.format(company_name=company_name)

    return script_part

def record_outcome(experiment_name: str, variant: str, score: float):
    """
    Records the outcome of a call for a specific variant.

    This is a stub function. In a real system, this would write to a database or analytics service.
    """
    print(f"Recorded outcome for {experiment_name} (Variant {variant}): Score {score}")