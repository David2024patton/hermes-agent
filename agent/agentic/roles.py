"""
Agentic Roles and Specialization System

Implements specialized agent roles for the agentic autonomy system.
"""

from typing import List, Dict, Optional
from dataclasses import dataclass

@dataclass
class AgentRole:
    """Definition of a specialized agent role"""
    name: str
    description: str
    capabilities: List[str]
    default_tools: List[str]

class RoleManager:
    """Manages agent roles and their capabilities"""
    
    def __init__(self):
        self.roles: Dict[str, AgentRole] = {
            "researcher": AgentRole(
                name="researcher",
                description="Specialized in research and information gathering",
                capabilities=["web_search", "document_analysis", "knowledge_synthesis"],
                default_tools=["web_search", "browser", "file_search"]
            ),
            "developer": AgentRole(
                name="developer",
                description="Specialized in code implementation and testing",
                capabilities=["code_writing", "testing", "debugging"],
                default_tools=["terminal", "code_execution", "file"]
            ),
            "tester": AgentRole(
                name="tester",
                description="Specialized in quality assurance and testing",
                capabilities=["test_design", "test_execution", "bug_reporting"],
                default_tools=["terminal", "browser", "test_framework"]
            ),
            "documenter": AgentRole(
                name="documenter",
                description="Specialized in documentation and knowledge capture",
                capabilities=["technical_writing", "diagram_creation", "knowledge_organization"],
                default_tools=["markdown", "diagram", "file"]
            ),
            "architect": AgentRole(
                name="architect",
                description="Specialized in system design and planning",
                capabilities=["system_design", "api_planning", "requirements_analysis"],
                default_tools=["diagram", "planning", "file"]
            )
        }
    
    def get_role(self, role_name: str) -> Optional[AgentRole]:
        """Get a role by name"""
        return self.roles.get(role_name)
    
    def add_role(self, role: AgentRole):
        """Add a new role"""
        self.roles[role.name] = role
    
    def get_role_capabilities(self, role_name: str) -> List[str]:
        """Get capabilities for a role"""
        role = self.get_role(role_name)
        return role.capabilities if role else []

# Global role manager instance
def get_role_manager() -> RoleManager:
    """Get the global role manager instance"""
    global _role_manager
    if _role_manager is None:
        _role_manager = RoleManager()
    return _role_manager

_role_manager: Optional[RoleManager] = None