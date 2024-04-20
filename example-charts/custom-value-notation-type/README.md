# django



> **:exclamation: This Helm Chart is deprecated!**



![Version: 0.2.1](https://img.shields.io/badge/Version-0.2.1-informational?style=flat-square) ![Type: ](https://img.shields.io/badge/Type--informational?style=flat-square) ![AppVersion: 3.1](https://img.shields.io/badge/AppVersion-3.1-informational?style=flat-square)



Generic chart for basic Django-based web app



**Homepage:** <https://www.djangoproject.com/>



## Maintainers

| Name | Email | Url |
| ---- | ------ | --- |
| Rizky Maulana Nugraha | <lana.pcfre@gmail.com> |  |




## Source Code

* <https://github.com/django/django>




## Requirements

 | Repository | Name | Version |
|------------|------|---------|
| @stable | nginx-ingress | 0.22.1 |
| file://../../postgis/v0.2.1 | postgis | 0.2.1 |
| file://../../common/v1.0.0 | common | 1.0.0 |




# Some Long Description

This is a sample README with custom overrides.
Check the template in [README.md.gotmpl](README.md.gotmpl).

In that file, we redefine the template definition of `chart.valueDefaultColumnRender`
for some custom `@notationType` such as `string/email`.

This chart README uses `chart.valuesSectionHtml` instead of `chart.valuesSection`.
Using HTML table directly instead of using Markdown table allows us to control the table
presentation, such as the height. This is especially useful for very long `values.yaml` file,
and you need to scroll both horizontally and vertically to navigate the values.

In the template file, we redefine `chart.valuesTableHtml` so that we use table height of
400px at most. Github can understand that attribute. The more sophisticated use case is if you
want to combine helm-docs with a Jamstack static generator where you can have your own page generated
from this README.

The customization can goes even further. Normally, you can't define anchor in markdown unless it is a heading. But you can do so easily using HTML tags.
You can override the column key renderer by adding an `id` attribute so that it can be referred.
This way, when you write markdown links like [ingress.tls.secretName](#ingress--tls--secretName), clicking the link
will take you to the value description row.

## Value Types

One of the benefit of using HTML table is we can make a simple tooltip and anchor.
For example, the value [global.adminEmail](#global--adminEmail) is annotated as type `string/email`. We create
the definition of the value type here and can be anchored by links with `#stringemail` hyperlinks.

We can also create custom type column renderer, where we can assign a tooltip for each type.
Try this out. Go navigate to [global.adminEmail](#global--adminEmail) value, hover on the value type `string/email`, you will then see
some tooltip. Clicking the type link will direct you back to it's relevant value type section below.

Other useful case is If the type is a known type, like
Kubernetes service type, you can anchor the type to redirect user to k8s documentation page to learn more.
Check the value [persistence.staticDir.accessModes](#persistence--staticDir--accessModes)

### string/email

{{- define "chart.valuetypes.email" }}
This value type is for a valid email address format. Such as owner@somedomain.org.
{{- end }}
{{ template "chart.valuetypes.email" . }}

## Notation Type

Another reason to use HTML table is because in some cases we want to custom-render the default value.

In helm chart templates, sometimes author designs the template to accept a go template string value.
That means, the template string can be processed by helm chart and be replaced with dynamic computed values, before it was
rendered to the chart. Although it is very useful and flexible to make the default value be dynamic,
it is not entirely obvious for the chart users to see a go template as value in a `values.yml`.
It would then be helpful to custom-render these default values in the helm README, so that it is not
treated as a pure JSON object (because the syntax highlighter would be incorrect).
Instead we can custom render the presentation so it would make sense to the user.

In our example here, any key with a type `tpl/xxx` would be rendered as `<pre></pre>`
HTML tag, in which we both put the key name and the YAML multiline modifier `|` to make
it really clear that the key accept a multiline string as value, because it would be rendered as
YAML object by helm after the values are interpolated/substituted.

Take a look at [extraPodEnv](#extraPodEnv). The `Default` column shows the key name `extraPodEnv`, the multiline YAML
modifier `|`, and the template string which contains some go string template syntax `{{"{{ }}"}}`.

You can also control the HTML styling directly. In some markdown viewer, the HTML tag and inline styles
are respected, so the custom styles can be seen. Combined with a Jamstack approach, you can
design your template to also incorporate some custom React styles or simple CSS.

In our example here, [global.adminEmail](#global--adminEmail) is annotated with `email` notationType.
This allows you to insert custom rendering code for email. For supported markdown viewer, like Visual Studio Code,
the default value will have `green` color, and if clicked will direct you to your default email composer.

The reason we have two separate annotation, value type and notation type, is because several different types
can have the same type renderer. For example, any type `tpl/xxx` is a go template string, so it will be rendered the same
in our docs if we annotate it with `@notationType -- tpl`.

## Customized Rendering

This README also shows some possible customization with doxy-helm. In the [README.md.gotmpl](README.md.gotmpl)
file, you can see that we modified the column `Key` to also be hyperlinked with the definition in `values.yaml`.
If you view this README.md files in GitHub and click the value's key, you will be directed to the
key location in the `values.yaml` file.

You can also render a raw string into the comments using `@raw` annotations.
You can jump to [sampleYaml](#sampleYaml) key and check it's description where it
uses HTML `<summary>` tag to collapse some part of the comments.

{{ define "chart.valueDefaultColumnRender" }}
{{- $defaultValue := (default .Default .AutoDefault)  -}}
{{- $notationType := .NotationType }}
{{- if (and (hasPrefix "`" $defaultValue) (hasSuffix "`" $defaultValue) ) -}}
{{- $defaultValue = (toPrettyJson (fromJson (trimAll "`" (default .Default .AutoDefault) ) ) ) -}}
{{- $notationType = "json" }}
{{- end -}}
{{- if (eq $notationType "tpl" ) }}
<pre lang="{{ $notationType }}">
{{ .Key }}: |
{{- $defaultValue | nindent 2 }}
</pre>
{{- else if (eq $notationType "email") }}
<a href="mailto:{{ $defaultValue }}" style="color: green;">"{{ $defaultValue }}"</a>
{{- else }}
<pre lang="{{ $notationType }}">
{{ $defaultValue }}
</pre>
{{- end }}
{{ end }}

{{ define "chart.typeColumnRender" }}
{{- if (eq .Type "string/email") }}
<a href="#stringemail" title="{{- template "chart.valuetypes.email" -}}">{{.Type}}</a>
{{- else if (eq .Type "k8s/storage/persistent-volume/access-modes" )}}
<a target="_blank"
   href="https://kubernetes.io/docs/concepts/storage/persistent-volumes/#access-modes"
   >{{- .Type }}</a>
{{- else }}
{{ .Type }}
{{- end }}
{{ end }}

{{ define "chart.valuesTableHtml" }}
<table height="400px" >
	<thead>
		<th>Key</th>
		<th>Type</th>
		<th>Default</th>
		<th>Description</th>
	</thead>
	<tbody>
	{{- range .Values }}
		<tr>
			<td id="{{ .Key | replace "." "--" }}"><a href="./values.yaml#L{{ .LineNumber }}">{{ .Key }}</a></td>
			<td>{{- template "chart.typeColumnRender" . -}}</td>
			<td>
				<div style="max-width: 300px;">{{ template "chart.valueDefaultColumnRender" . }}</div>
			</td>
			<td>{{ if .Description }}{{ .Description }}{{ else }}{{ .AutoDescription }}{{ end }}</td>
		</tr>
	{{- end }}
	</tbody>
</table>
{{ end }}

{{ template "chart.valuesSectionHtml" . }}

Autogenerated from chart metadata using [helm2readme v1.0.1](https://github.com/tactful-ai/helm2readme)
