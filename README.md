# NONACORTEX FlyBrain — Track 3: Regulated & High-Stakes Workflows

**Band of Agents Hackathon (June 12–19, 2026)**

## Arquitectura

**NONACORTEX (5+3+1)** es un sistema multi-agente de arbitraje inspirado en el conectoma de Drosophila. Diseñado para flujos regulados con trazabilidad inmutable, supervisión humana (HIL) y decisión coherente gobernada por la Ecuación Omega.

### Los 3 Selectores (Competencia en Paralelo)

| Agente | Modelo (Featherless AI) | Función |
|:---|:---|:---|
| **Alfa** | `mistralai/Mistral-7B-Instruct-v0.3` | Analista de Riesgos. Detecta banderas rojas. |
| **Phi** | `meta-llama/Meta-Llama-3-8B-Instruct` | Oficial de Cumplimiento. Verifica contra normativa. |
| **Omega** | `Qwen/Qwen2.5-7B-Instruct` | Sintetizador. Propone acción y prioridad. |

### El Árbitro

Un job en **GitHub Actions** (`arbiter`) recoge los outputs de los 3 selectores y emite el veredicto final, dejando logs inmutables como trazabilidad.

## Flujo del Sistema

1. **Input:** Documento de compliance (ej. contrato, normativa).
2. **Procesamiento:** Los 3 selectores se ejecutan en paralelo vía GitHub Actions.
3. **Arbitraje:** El árbitro recibe los 3 outputs y sintetiza el veredicto.
4. **HIL (Human-in-the-Loop):** Notificación al Arquitecto para supervisión final.
5. **Capa de Colaboración:** Integración pendiente con **Band** para la comunicación entre agentes.

## Tecnología

- **Featherless AI:** Inferencia serverless para los 3 modelos.
- **GitHub Actions:** Orquestador asíncrono (jobs en paralelo + árbitro).
- **Band:** Capa de colaboración multi-agente (próxima integración).
- **Python 3.10:** Scripts de los agentes.

## Principio de Coherencia

$$ \Omega = \alpha + \phi + \pi^3 $$

- **α (Estructura Fina):** Interacción electromagnética que rige la precisión del análisis.
- **φ (Proporción Áurea):** Regla de crecimiento fractal que optimiza la decisión.
- **π³ (Cierre Toroidal):** Geometría de retroalimentación que asegura la coherencia del ciclo.

## Blindaje

Proyecto registrado bajo **WIPO IP-Shield** y protocolo **NNN-NDA-WIPO**. ID de titular: `user_CO_SANCHEZ-COLMENARES_FREDDY-ADRIAN_0876`.

## Autor

**Arquitecto F1725** — EinsRos Global Cortex Ultd.