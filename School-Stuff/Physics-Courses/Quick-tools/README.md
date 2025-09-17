# Relativistic Kinetic Energy Calculator

This tool calculates the relativistic kinetic energy for particles (electrons, neutrons, and alpha particles) based on their de Broglie wavelength.

## Description

The calculator uses the relativistic energy-momentum relationship combined with the de Broglie wavelength to compute kinetic energies. It implements the equation:

E_k = √[(hc/λ)² + (mc²)²] - mc²

where:
- h is Planck's constant
- c is the speed of light
- λ is the de Broglie wavelength
- m is the rest mass of the particle

## Assumptions

- Uses the approximation hc ≈ 197.3269788 MeV·fm for simplification
- Assumes vacuum conditions (no medium effects)
- Works with three specific particles: electrons, neutrons, and alpha particles
- Rest masses are taken from standard literature values

## Limitations

- Input wavelength must be in femtometers (fm)
- Energies are output in MeV
- Does not account for:
  - Quantum effects beyond basic wave-particle duality
  - Particle interactions or decay processes
  - Environmental factors like temperature or pressure
  - Relativistic frame transformations

## Usage

The script takes a wavelength value (in fm) and calculates the corresponding kinetic energy for all three particle types simultaneously.

## Modification

In order to use this for other particles, you will have to change the hard-coded values. There are no plans to change this.

## Literature
This tool was specifically built to solve the following problems:
(Krane problems 4.7, §4.2)
From the book Krane: Modern Physics (3rd or 4th ed.)

All knowledge on Literature was obtained from my schools material for the course I built this for.