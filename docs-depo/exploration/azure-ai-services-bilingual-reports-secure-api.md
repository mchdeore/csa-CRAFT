# Azure AI Services Research: Bilingual Report Generation and Secure API Exposure for CRAFT

**Date**: 2026-09-29  
**Focus**: UMR-046 (Bilingual Reports) + Secure Connector Routes  
**Scope**: Translation, NLG, Vector Search, API Gateway architecture

---

## Executive Summary

This research evaluates Azure services for three key capabilities required by UMR-046 and related CRAFT requirements:

1. **Bilingual content generation** — Azure OpenAI GPT-4o mini + Azure Translator
2. **Vector search for RAG evidence retrieval** — Azure AI Search (Serverless vs Dedicated)
3. **Secure API exposure for external connectors** — API Management + Application Gateway

**Key findings**:
- Report generation is cheap (~$17/month for 100 reports) — the real cost is vector search infrastructure
- Azure AI Search Serverless is 10-20x cheaper than Dedicated for business-hours usage
- APIM + Application Gateway provides defense-in-depth for connector security

---

## Problem Statement

UMR-046 requires the system to generate bilingual (English/French) reports using approved CSA templates. This involves:
1. Report generation from structured data and evidence
2. Translation of narrative content between English and French
3. Template-based document assembly
4. Secure exposure of the report generation endpoint for external connectors

**Dependency note**: Report generation requires RAG evidence retrieval (UMR-003 through UMR-006), which means Azure AI Search is a prerequisite.

---

## Azure Service Options

### 1. Azure AI Translator (for Translation)

**Service**: Azure Translator in Foundry Tools

**Pricing** (as of 2026-09-29):
- **Free Tier (F0)**: 2 million characters/month free
- **Pay-as-you-go (S1)**: ~$10/million characters for standard translation
- **Document Translation**: Same rate per character, includes preserving formatting
- **Commitment Tiers**: Discounted rates for high volume (250M+ characters)

**Key Features for Bilingual Reports**:
- Real-time text translation via REST API
- **Document Translation API**: Translates entire documents while preserving structure/formatting (Word, PDF, HTML)
- Custom Translation: Train models on CSA-specific terminology for consistent translations
- Supports 100+ languages including French-English pair
- Dictionary lookup and transliteration

**Cost Estimate**:
- A 20-page report ≈ 50,000 characters
- 100 reports/month ≈ 5M characters ≈ $50/month at S1 rates
- Free tier covers initial development/testing

**Recommendation**: Use Azure Translator Document Translation API for preserving template formatting. Consider Custom Translation for CSA-specific aerospace terminology.

---

### 2. Azure OpenAI GPT-4o mini (for Natural Language Generation)

**Service**: Azure OpenAI Service - GPT-4o mini model

**Pricing** (as of 2026-09-29):
- **Input**: $0.15-$0.165 per 1M tokens
- **Output**: $0.60-$0.66 per 1M tokens
- **128K context window**, up to 16K output tokens
- **Batch API**: 50% discount for 24-hour turnaround

**Key Features for Report Generation**:
- Structured output (JSON mode) for consistent report sections
- Strong at synthesizing evidence into narrative text
- Can follow template structures and formatting instructions
- Multilingual capability (generate directly in EN/FR rather than translate)
- Function calling for integrating with evidence retrieval

**Cost Estimate**:
- Generating a 20-page report ≈ 15,000 input tokens + 8,000 output tokens
- 100 reports/month ≈ $1.50 input + $5.28 output ≈ $7/month
- Very cost-effective compared to larger models

**Recommendation**: Use GPT-4o mini for report generation. Generate content in both languages directly rather than post-translation for more natural output. Use structured output to ensure template compliance.

---

### 3. Secure Route Exposure for Connectors

**Service**: Azure API Management (APIM) + Application Gateway

**Architecture Pattern**: Internal VNet + Application Gateway front door

**How It Works**:
1. **APIM in Internal VNet Mode**: API Management deployed inside virtual network, accessible only internally
2. **Application Gateway as Front Door**: Layer-7 load balancer with WAF, exposes select APIs externally
3. **Selective Exposure**: Route only `/reports` endpoints through Application Gateway, keep internal APIs private
4. **Security Layers**:
   - Web Application Firewall (WAF) blocks malicious requests
   - OAuth 2.0 / Microsoft Entra ID authentication
   - Rate limiting and throttling
   - IP whitelisting for partner connectors
   - API keys/subscriptions for external consumers

**Key Benefits**:
- Single APIM instance serves both internal and external consumers
- Subset of APIs exposed externally (only report generation, not internal tools)
- Turnkey on/off switch for external access
- Full audit logging of all API calls
- MCP server support: APIM can expose REST APIs as MCP servers for AI agents

**Recommendation**: Deploy APIM in internal VNet with Application Gateway. Configure path-based routing to expose only `/reports/*` endpoints. Use Entra ID OAuth for connector authentication.

---

## Azure AI Search (Vector Store for RAG)

Report generation requires evidence retrieval via RAG. UMR-003 through UMR-006 require a vector store with hybrid search, which means Azure AI Search is a prerequisite dependency.

### Serverless vs Dedicated Pricing Comparison

**Source**: Microsoft Copilot estimates (2026-09-29), validated against Azure AI Search pricing model.

| Scenario | Data Size | Searches/Day | Searches/Month | Serverless Est. | Dedicated Est. |
|-----------|----------:|-------------:|---------------:|----------------:|---------------:|
| Hobby project | 10 GB | 5 | 150 | $1 - $10 | $75 - $150 |
| Small team | 50 GB | 100 | 3,000 | $10 - $50 | $100 - $250 |
| Department bot | 100 GB | 250 | 7,500 | $20 - $80 | $150 - $400 |
| Medium organization | 250 GB | 500 | 15,000 | $50 - $200 | $250 - $800 |
| Heavy internal tool | 250 GB | 2,000 | 60,000 | $150 - $500+ | $500 - $1,500+ |

### Key Assumptions

**Serverless**:
- Business-hours usage (scales to zero overnight)
- Vector search enabled
- Infrequent to moderate document updates
- No heavy OCR/AI enrichment pipeline

**Dedicated**:
- Service runs 24/7
- Billing based on provisioned capacity (replicas × partitions), not actual usage
- High availability requires additional replicas even with low utilization

### Quick Reference

| Usage Pattern | Serverless | Dedicated |
|---------------|------------|-----------|
| 5 searches/day | $1-$10/mo | $75-$150/mo |
| 100 searches/day | $10-$50/mo | $100-$250/mo |
| 500 searches/day, 250 GB | $50-$200/mo | $250-$800/mo |
| 2000 searches/day, 250 GB | $150-$500/mo | $500-$1,500+/mo |

### Recommendation for CRAFT

For an internal RAG chatbot with business-hours usage and a few hundred users:
- **Serverless is significantly cheaper** until usage becomes large and predictable
- Start with Serverless, monitor actual query volume
- Consider migrating to Dedicated S1/S2 only if:
  - Query latency becomes a problem (need dedicated capacity)
  - Usage exceeds ~60,000 searches/month consistently
  - You need 24/7 SLA guarantees

**Estimated CRAFT usage**: 100-500 searches/day across all agent operations (reports, Q&A, analysis)
- Recommended: **Azure AI Search Serverless**
- Budget: $20-$200/month depending on document corpus size and query volume

---

## Implementation Recommendation

### Architecture Overview

```
External Connector → Application Gateway (WAF) → APIM (internal VNet) → CRAFT API → Report Engine
                                                              ↓
                                        ┌─────────────────────┴─────────────────────┐
                                        │                                           │
                                   Azure OpenAI                            Azure Translator
                                   (GPT-4o mini)                           (Document Translation)
                                        │                                           │
                                        └─────────────────────┬─────────────────────┘
                                                              ↓
                                                    Bilingual Report Output
```

### Workflow

1. **Report Request** → Connector calls `/reports/generate` via Application Gateway
2. **Authentication** → APIM validates OAuth token / API key
3. **Evidence Retrieval** → CRAFT agent retrieves relevant documents via RAG
4. **Report Generation** → GPT-4o mini synthesizes evidence into structured report sections
5. **Bilingual Output** → Either:
   - Generate directly in both languages (preferred for natural text)
   - Generate in one language, translate via Azure Translator (for consistency)
6. **Template Assembly** → Populate approved Word/PDF templates
7. **Delivery** → Return bilingual report package via API response or SharePoint

---

## Cost Summary

### Estimated Monthly Cost (100 reports)

**Note**: The estimates below cover only report generation (NLG + translation). **Vector search infrastructure for RAG is a separate major cost driver**.

#### Report Generation Costs

| Service | Usage | Cost |
|---------|-------|------|
| Azure OpenAI GPT-4o mini | 100 reports × 23K tokens | ~$7 |
| Azure Translator | 100 reports × 100K chars (if needed) | ~$10 |
| **Report Generation Subtotal** | | **~$17/month** |

#### Infrastructure Costs (Shared)

| Service | Usage | Cost |
|---------|-------|------|
| APIM (Developer tier) | 1 instance | ~$50 |
| Application Gateway (WAF_v2) | 2 instances | ~$350 |
| **Infrastructure Subtotal** | | **~$400/month** |

#### Vector Search Costs

| Service | Usage Pattern | Cost |
|---------|---------------|------|
| Azure AI Search Serverless | 100-500 searches/day, 100-250 GB | $20-$200/month |
| Azure AI Search Dedicated | 100-500 searches/day, 100-250 GB | $150-$800/month |

**Total estimated monthly cost for UMR-046 capability**: 
- With Serverless: ~$440-$620/month (infrastructure + vector search + report gen)
- With Dedicated: ~$570-$1,200/month

Note: APIM and Application Gateway are infrastructure costs shared across all requirements, not just UMR-046.

---

## Next Steps

1. **Template Inventory**: Collect CSA-approved report templates (Word format preferred)
2. **Terminology Baseline**: Build bilingual glossary of CSA aerospace terms for Custom Translation
3. **API Design**: Define `/reports/generate` endpoint schema and authentication requirements
4. **Pilot Implementation**: Build minimal report generation flow with GPT-4o mini
5. **Evaluate Direct Generation vs Translation**: A/B test quality of directly-generated bilingual content vs translated content

---

## References

- [Azure Translator Pricing](https://azure.microsoft.com/en-us/pricing/details/cognitive-services/translator/)
- [Azure OpenAI Pricing](https://azure.microsoft.com/en-us/pricing/details/azure-openai/)
- [APIM with Application Gateway Integration](https://learn.microsoft.com/en-us/azure/api-management/api-management-howto-integrate-internal-vnet-appgateway)
- [GPT-4o mini Model Card](https://developers.openai.com/api/docs/models/gpt-4o-mini)
