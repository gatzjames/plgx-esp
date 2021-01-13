{{/*
Create a default fully qualified app name.
We truncate at 63 chars because some Kubernetes name fields are limited to this (by the DNS naming spec).
If release name contains chart name it will be used as a full name.
*/}}
{{- define "polylogyx.fullname" -}}
{{- default .Chart.Name .Values.nameOverride | trunc 63 | trimSuffix "-" -}}
{{- end -}}

{{/*
Return the rsyslogf pvc name.
*/}}
{{- define "polylogyx.rsyslogf.pvcName" -}}
{{- .Values.plgx.rsyslogf.persistence.existingClaim | default (printf "%s-rsyslogf-pvc" (include "polylogyx.fullname" .)) -}}
{{- end -}}


{{/*
Return the yara pvc name
*/}}
{{- define "polylogyx.yara.pvcName" -}}
{{- .Values.plgx.persistence.yara.existingClaim | default (printf "%s-yara-pvc" (include "polylogyx.fullname" .)) -}}
{{- end -}}

{{/*
Return the yara pvc storageClass
*/}}
{{- define "polylogyx.yara.storageClass" -}}
{{- $storageClass := .Values.plgx.persistence.yara.storageClass -}}

{{- if $storageClass -}}
  {{- if (eq "-" $storageClass) -}}
      {{- printf "storageClassName: \"\"" -}}
  {{- else }}
      {{- printf "storageClassName: %s" $storageClass -}}
  {{- end -}}
{{- end -}}
{{- end -}}

{{/*
Return the carves pvc storageClass
*/}}
{{- define "polylogyx.carves.storageClass" -}}
{{- $storageClass := .Values.plgx.persistence.carves.storageClass -}}

{{- if $storageClass -}}
  {{- if (eq "-" $storageClass) -}}
      {{- printf "storageClassName: \"\"" -}}
  {{- else }}
      {{- printf "storageClassName: %s" $storageClass -}}
  {{- end -}}
{{- end -}}
{{- end -}}

{{/*
Return the carves pvc name
*/}}
{{- define "polylogyx.carves.pvcName" -}}
{{- .Values.plgx.persistence.carves.existingClaim | default (printf "%s-carves-pvc" (include "polylogyx.fullname" .)) -}}
{{- end -}}

{{- define "polylogyx.pvcs.storageClass" -}}

{{- $storageClass := .Values.plgx.persistence.storageClass -}}

{{- if $storageClass -}}
  {{- if (eq "-" $storageClass) -}}
      {{- printf "storageClassName: \"\"" -}}
  {{- else }}
      {{- printf "storageClassName: %s" $storageClass -}}
  {{- end -}}
{{- end -}}

{{- end -}}

{{- define "polylogyx.rsyslogf.storageClass" -}}

{{- $storageClass := default .Values.plgx.persistence.storageClass .Values.plgx.rsyslogf.persistence.storageClass -}}

{{- if $storageClass -}}
  {{- if (eq "-" $storageClass) -}}
      {{- printf "storageClassName: \"\"" -}}
  {{- else }}
      {{- printf "storageClassName: %s" $storageClass -}}
  {{- end -}}
{{- end -}}

{{- end -}}