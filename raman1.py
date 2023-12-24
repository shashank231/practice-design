from pydantic import BaseModel as PyBaseModel, Extra
from typing import Optional, List

class BaseModel(PyBaseModel):
    critical_priority: Optional[int] = None
    class Config:
        extra = Extra.forbid

class MonitorSettings(BaseModel):
    critical_priority: int = 1
    warning_priority: int = 2

class BaseJobMonitorSettings(MonitorSettings):
    pass

class FailureMonitorSettings(BaseJobMonitorSettings):
    critical_threshold: int = 2
    timeout_h: Optional[int] = 3

class RuntimeMonitorSettings(BaseJobMonitorSettings):
    critical_threshold: float = 4
    timeout_h: Optional[int] = 5

class CronjobMonitorSettings(BaseModel):
    resource_id: str
    # critical_priority: Optional[int] = None
    warning_priority: Optional[int] = None
    failure_monitor_settings: FailureMonitorSettings = FailureMonitorSettings()
    runtime_monitor_settings: RuntimeMonitorSettings = RuntimeMonitorSettings()


class CronjobMonitorSetArgs(BaseModel):
    environment: str
    # critical_priority: Optional[int] = None
    warning_priority: Optional[int] = None
    monitor_settings: List[CronjobMonitorSettings] = []
    class Config:
        arbitrary_types_allowed = True

class CronjobMonitorSet:
    def __init__(self, args: CronjobMonitorSetArgs) -> None:
        self.args = args

a1 = CronjobMonitorSet(
            args=CronjobMonitorSetArgs(
                critical_priority=150,
                environment="prod1",
                monitor_settings=[
                    CronjobMonitorSettings(
                        critical_priority=200,
                        resource_id="id1",
                        failure_monitor_settings=FailureMonitorSettings(
                            critical_priority=250,
                            critical_threshold=3,
                        ),
                        runtime_monitor_settings=RuntimeMonitorSettings(
                            critical_threshold=3,
                        ),
                    ),
                    CronjobMonitorSettings(
                        resource_id="id2",
                        failure_monitor_settings=FailureMonitorSettings(
                            critical_threshold=4,
                        ),
                    ),
                ],
            ),
        )

print(a1)

import pdb
pdb.set_trace()



















