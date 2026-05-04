import importlib
import sys


class BlockPydanticAiImports:
    def find_spec(self, fullname, path=None, target=None):
        if fullname == "pydantic_ai" or fullname.startswith("pydantic_ai."):
            raise AssertionError(f"Unexpected import of {fullname}")
        return None


def test_generative_ai_registries_do_not_import_pydantic_ai_on_startup(monkeypatch):
    for module_name in list(sys.modules):
        if (
            module_name == "baserow.core.generative_ai.registries"
            or module_name == "pydantic_ai"
            or module_name.startswith("pydantic_ai.")
        ):
            monkeypatch.delitem(sys.modules, module_name, raising=False)

    monkeypatch.setattr(
        sys, "meta_path", [BlockPydanticAiImports(), *sys.meta_path]
    )

    importlib.import_module("baserow.core.generative_ai.registries")
