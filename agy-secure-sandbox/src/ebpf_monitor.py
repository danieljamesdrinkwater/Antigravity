"""
AGY Secure Sandbox
Mock eBPF kernel-level monitoring for secure MCP execution.
"""

class SandboxMonitor:
    def __init__(self, egress_policy: str = "strict"):
        self.egress_policy = egress_policy
        self.active_processes = set()

    def attach_ebpf_probe(self, process_id: int):
        """
        Simulates attaching an eBPF probe to monitor system calls.
        """
        self.active_processes.add(process_id)
        return f"eBPF probe attached to PID {process_id}."

    def validate_network_call(self, process_id: int, destination: str) -> bool:
        """
        Enforces strict network egress policies on isolated MCP servers.
        """
        if process_id not in self.active_processes:
            return False
            
        if self.egress_policy == "strict":
            # Only allow loopback or trusted AGY ports in strict mode
            if destination.startswith("127.0.0.1") or destination.startswith("localhost"):
                return True
            return False
        return True
