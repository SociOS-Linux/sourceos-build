variable "environment" {
  type        = string
  description = "Target environment (e.g. dev, prod)."
}

variable "build_namespace" {
  type        = string
  description = "Kubernetes namespace for build pipelines."
  default     = "sourceos-build"
}
