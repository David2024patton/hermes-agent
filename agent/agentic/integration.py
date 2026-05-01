"""
Integration of Agentic System with Hermes Agent Core

This module connects the agentic autonomy features to the main Hermes Agent system.
"""

from typing import Dict, Any, Optional
from agent.agentic import get_agentic_system
from agent.agentic.roles import get_role_manager
from agent.agentic.coordination import get_agentic_coordinator

class AgenticIntegration:
    """Main integration class for agentic features"""
    
    def __init__(self):
        self.agentic_system = get_agentic_system()
        self.role_manager = get_role_manager()
        self.coordinator = get_agentic_coordinator()
    
    def execute_agentic_task(self, task_description: str) -> Dict:
        """Execute a task using the full agentic system"""
        return self.agentic_system.execute_task(task_description)
    
    def get_available_roles(self) -> Dict:
        """Get available agent roles"""
        roles = {}
        for role_name, role in self.role_manager.roles.items():
            roles[role_name] = {
                "description": role.description,
                "capabilities": role.capabilities,
                "default_tools": role.default_tools
            }
        return roles
    
    def get_system_status(self) -> Dict:
        """Get current agentic system status"""
        return self.coordinator.get_system_status()
    
    def add_custom_role(self, role_name: str, description: str, 
                       capabilities: list, default_tools: list) -> bool:
        """Add a custom agent role"""
        from agent.agentic.roles import AgentRole
        
        if role_name in self.role_manager.roles:
            return False
            
        new_role = AgentRole(
            name=role_name,
            description=description,
            capabilities=capabilities,
            default_tools=default_tools
        )
        self.role_manager.add_role(new_role)
        return True

# Global integration instance
def get_agentic_integration() -> AgenticIntegration:
    """Get the global agentic integration instance"""
    global _agentic_integration
    if _agentic_integration is None:
        _agentic_integration = AgenticIntegration()
    return _agentic_integration

_agentic_integration: Optional[AgenticIntegration] = None