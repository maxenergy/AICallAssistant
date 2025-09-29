from intelligent_outbound_ai.core.models import CompanyProfile

def get_company_profile(company_name: str) -> CompanyProfile:
    """
    Retrieves a company's profile based on its name.

    This is a stub function that returns a mock profile.
    """
    return CompanyProfile(
        name=company_name,
        industry="科技",
        recent_news="最近发布了新的产品线，市场反响热烈。",
        key_personnel=["张三 (CEO)", "李四 (CTO)"],
        potential_needs=["扩大市场份额", "提升研发效率"]
    )