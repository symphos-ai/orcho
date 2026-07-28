"""Project-local Orcho configuration for the ``orcho`` distribution package."""

PLUGIN = {
    "name": "orcho-dist",
    "language": "Python 3.12+",
    "architecture": (
        "Thin public distribution package that owns packaging metadata and "
        "console-script dispatch into the Orcho component packages."
    ),
    "file_hints": [
        "src/orcho/",
        "tests/",
        "pyproject.toml",
        ".github/workflows/",
    ],
    "dependency_repos": {
        "orcho-core": {
            "path": "../orcho-core",
            "required": True,
        },
        "orcho-mcp": {
            "path": "../orcho-mcp",
            "required": True,
        },
    },
    "work_mode": "pro",
    "verification_envs": {
        "dist-local": {
            "python": "{project}/.venv/bin/python",
            "cwd": "{checkout}",
            "env": {
                "PYTHONPATH": "{checkout}/src:{checkout}",
            },
            "assertions": [
                {"file_exists": "{project}/.venv/bin/python"},
                {
                    "import": "orcho",
                    "path_under": "{checkout}/src/orcho",
                },
                {"file_exists": "pyproject.toml"},
                {"version": ["python", "--version"], "contains": "Python 3."},
            ],
        },
    },
    "verification": {
        "default_env": "dist-local",
        "delivery_policy": "require",
        "required": [
            "env-provenance",
            "lint",
            "test-unit",
        ],
        "commands": {
            "env-provenance": {
                "env": "dist-local",
                "cost": "fast",
                "run": [
                    "python",
                    "-c",
                    (
                        "import orcho; "
                        "p = orcho.__file__; "
                        "assert 'site-packages' not in p and 'dist-packages' "
                        "not in p, ('orcho resolved to an installed copy, not "
                        "the checkout under review: ' + p); "
                        "print('orcho:', p)"
                    ),
                ],
            },
            "lint": {
                "env": "dist-local",
                "cost": "fast",
                "run": ["python", "-m", "ruff", "check", "."],
            },
            "test-unit": {
                "env": "dist-local",
                "cost": "moderate",
                "parity": "differential",
                "run": ["python", "-m", "pytest", "-q", "tests"],
            },
        },
        "gate_sets": {
            "provenance": {
                "commands": ["env-provenance"],
                "default_policy": "require",
                "default_action": "handoff",
                "default_cost": "fast",
            },
            "hygiene": {
                "commands": ["lint"],
                "default_policy": "require",
                "default_action": "repair_loop",
                "default_cost": "fast",
            },
            "tests": {
                "commands": ["test-unit"],
                "default_policy": "require",
                "default_action": "repair_loop",
                "default_cost": "moderate",
            },
        },
        "selection": [
            {"always": ["provenance", "hygiene", "tests"]},
        ],
        "schedule": [
            {
                "after_phase": "implement",
                "gate_sets": ["provenance"],
                "policy": "require",
                "action": "handoff",
            },
            {
                "after_phase": "implement",
                "gate_sets": ["hygiene", "tests"],
                "policy": "require",
                "action": "repair_loop",
            },
        ],
    },
}
