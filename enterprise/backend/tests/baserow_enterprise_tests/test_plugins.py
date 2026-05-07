import importlib
import sys


class BlockPydanticAiImports:
    def find_spec(self, fullname, path=None, target=None):
        if fullname == "pydantic_ai" or fullname.startswith("pydantic_ai."):
            raise AssertionError(f"Unexpected import of {fullname}")
        return None


def test_enterprise_plugin_import_does_not_import_pydantic_ai(monkeypatch):
    for module_name in list(sys.modules):
        if (
            module_name == "baserow_enterprise.plugins"
            or module_name.startswith("baserow_enterprise.api.assistant")
            or module_name == "pydantic_ai"
            or module_name.startswith("pydantic_ai.")
        ):
            monkeypatch.delitem(sys.modules, module_name, raising=False)

    monkeypatch.setattr(
        sys, "meta_path", [BlockPydanticAiImports(), *sys.meta_path]
    )

    importlib.import_module("baserow_enterprise.plugins")


def test_assistant_tool_type_imports_do_not_import_pydantic_ai(monkeypatch):
    for module_name in list(sys.modules):
        if (
            module_name.startswith("baserow_enterprise.assistant.tools")
            or module_name == "baserow_enterprise.assistant.deps"
            or module_name == "pydantic_ai"
            or module_name.startswith("pydantic_ai.")
        ):
            monkeypatch.delitem(sys.modules, module_name, raising=False)

    monkeypatch.setattr(
        sys, "meta_path", [BlockPydanticAiImports(), *sys.meta_path]
    )

    for module_name in [
        "baserow_enterprise.assistant.tools.automation.tool_types",
        "baserow_enterprise.assistant.tools.builder.tool_types",
        "baserow_enterprise.assistant.tools.core.tool_types",
        "baserow_enterprise.assistant.tools.database.tool_types",
        "baserow_enterprise.assistant.tools.navigation.tool_types",
        "baserow_enterprise.assistant.tools.search_user_docs.tool_types",
    ]:
        importlib.import_module(module_name)


def test_assistant_tasks_import_does_not_import_pydantic_ai(monkeypatch):
    for module_name in list(sys.modules):
        if (
            module_name == "baserow_enterprise.assistant.tasks"
            or module_name == "baserow_enterprise.assistant.handler"
            or module_name == "baserow_enterprise.assistant.assistant"
            or module_name == "pydantic_ai"
            or module_name.startswith("pydantic_ai.")
        ):
            monkeypatch.delitem(sys.modules, module_name, raising=False)

    monkeypatch.setattr(
        sys, "meta_path", [BlockPydanticAiImports(), *sys.meta_path]
    )

    importlib.import_module("baserow_enterprise.assistant.tasks")


def test_assistant_urls_import_does_not_import_pydantic_ai(monkeypatch):
    for module_name in list(sys.modules):
        if (
            module_name.startswith("baserow_enterprise.api.assistant")
            or module_name == "baserow_enterprise.assistant.assistant"
            or module_name == "baserow_enterprise.assistant.model_profiles"
            or module_name == "pydantic_ai"
            or module_name.startswith("pydantic_ai.")
        ):
            monkeypatch.delitem(sys.modules, module_name, raising=False)

    monkeypatch.setattr(
        sys, "meta_path", [BlockPydanticAiImports(), *sys.meta_path]
    )

    importlib.import_module("baserow_enterprise.api.assistant.urls")
