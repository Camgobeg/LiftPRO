# LiftPRO

A detailed elevator simulation mod for **Minecraft Java 1.20.1 / Forge 47 / Java 17**.

LiftPRO targets the visual language and interaction quality of modern premium MRL elevators: brushed-metal fixtures, glass cabins, precision door motion, destination dispatch, hall lanterns, rope and counterweight visuals, machine-room layouts and service controls. All models, textures, sounds and UI are intended to be original; commercial elevator brands are inspiration only, not assets to copy.

## Build
Use JDK 17 and Gradle 8.8:
```bash
gradle clean test build
```
The distributable jar is in `build/libs/`. GitHub Actions runs the same build on pushes and pull requests and uploads the jar as an artifact.

## Design pillars
- Server-authoritative motion and dispatch.
- Distinct MR traction and MRL machine layouts.
- Moving cabin with passenger support and synchronized doors.
- Counterweight, traction sheave, rope bundle and guide rail visualization.
- Hall fixtures, car operating panels, lanterns and service modes.
- Original destination-dispatch UX inspired by modern elevator systems.

## Status
Early development. The first milestone is a stable Forge bootstrap and CI pipeline; visual/gameplay systems are being implemented incrementally. A registered block is not a finished feature until its model, interaction, persistence and multiplayer behavior are complete.
