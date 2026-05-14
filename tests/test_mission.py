from physical_ai_lab.mission import scenario_by_id, signature_scenarios


def test_signature_scenarios_have_evidence_and_business_value() -> None:
    scenarios = signature_scenarios()

    assert len(scenarios) >= 3
    for scenario in scenarios:
        assert scenario.identifier
        assert scenario.hardware
        assert scenario.software
        assert scenario.requirements
        assert all(requirement.evidence for requirement in scenario.requirements)
        assert all(requirement.business_value for requirement in scenario.requirements)


def test_scenario_lookup_by_id() -> None:
    scenario = scenario_by_id("yahboom-mobile-manipulation")

    assert scenario.title.startswith("Yahboom")
    assert scenario.readiness_score == 0.0
