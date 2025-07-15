# Event Storming: Metadata Management

[Event storming](https://www.eventstorming.com/) is a collaborative technique used for domain discovery. It is typically conducted in a workshop setting and allows the stakeholders of a given domain to build a high-level model of its systems and related processes. While many concepts from [Domain-Driven Design](https://github.com/ddd-crew/welcome-to-ddd) are used in event storming, it is not a strictly DDD focused technique.

Most of the online resources related to event storming will show examples that are business domain oriented. We have taken the basic concepts from event storming and modified them to model the systems and processes involved in ProtoDUNE metadata management.

## Notation

There are many commonly adopted patterns for notation in event storming, but you will often see variation in the definitions, the color palette, and the flow of interactions that are used by different practitioners. As a general practice interactions, are time ordered; flowing from left to right, and from top to bottom. The following describes the basic notation used in the design of the ProtoDUNE metadata management process models.

!!! diagram "Event Storming Notation"
    ![Alt text](../images/es-notation.drawio.svg "Event Storming Notation")

| Notation Type                                                               | Description                                                                     |
| --------------------------------------------------------------------------- | ------------------------------------------------------------------------------- |
| `Bounded Context (Dashed Box)`{ .table-colors-black }                       | An area of domain language consistency. A way to group all related domain events, entities, and their processes. |
| `Actor (Light Yellow)`{ .table-colors-light-yellow }                        | The users that participate in any process; they can be human, or computational. |
| `Command (Blue)`{ .table-colors data-md-color-primary="blue" }              | The execution of an action. |
| `Domain Event (Orange)`{ .table-colors-orange }                             | The result of an executed action. Considered the facts of a domain. |
| `External System (Pink)`{ .table-colors-light-pink }                        | External platforms, APIs, sites, etc. |
| `Policy (Purple)`{ .table-colors data-md-color-primary="deep-purple" }      | A process that is called when something happens. |
| `Aggregate (Yellow)`{ .table-colors data-md-color-primary="yellow" }        | A top-level entity that encapsulates all of the domain rules, including the child entities involved in command execution. |
| `Read Model (Green)`{ .table-colors data-md-color-primary="green" }         | Data that needs to fetched from a source; often used to make process decisions. |
| `Hotspot (Red)`{ .table-colors data-md-color-primary="red" }                | Possible issues or items that we do not yet know how to handle. |
| `Comment (Light Grey)`{ .table-colors-light-grey }                          | A callout indicating something of note. |

## Metadata Management Process Models

### Interval of Validity (IOV)
!!! diagram "ProtoDUNE Interval of Validity Model"
    ![Alt text](../images/es-iov-metadata.drawio.svg "ProtoDUNE Interval of Validity Metadata Management Process Model")

### Run Configuration
!!! diagram "ProtoDUNE Run Configuration Process Model"
    ![Alt text](../images/es-config-metadata.drawio.svg "ProtoDUNE Run Configuration Metadata Management Process Model")

### Beam Conditions (IFBeam)
!!! diagram "ProtoDUNE Beam Conditions Process Model"
    ![Alt text](../images/es-beam-metadata.drawio.svg "ProtoDUNE Beam Conditions Metadata Management Process Model")

### Slow Controls
!!! diagram "ProtoDUNE Slow Controls Process Model"
    ![Alt text](../images/es-slow-controls-metadata.drawio.svg "ProtoDUNE Slow Controls Metadata Management Process Model")

### Offline Calibration
!!! diagram "ProtoDUNE Calibration Process Model"
    ![Alt text](../images/es-calibration-metadata.drawio.svg "ProtoDUNE Calibration Metadata Management Process Model")

### Simulation
!!! diagram "ProtoDUNE Simulation Metadata Management Process Model"
    ![Alt text](../images/es-simulation-metadata.drawio.svg "ProtoDUNE Simulation Metadata Management Process Model")

### Data Quality and Monitoring (DQM)
!!! warning "(TBD) ProtoDUNE Data Quality and Monitoring Process Model"
