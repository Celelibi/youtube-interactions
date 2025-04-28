#!/usr/bin/env python3

"""This program generates a YouTubeMixin class from the discovery API of
google. All the methods have a docstring containing whatever documentation was
available in the JSON from the API. All the arguments required by the Youtube
Data API are also required by the python methods. All the method names and
argument names are translated to the PEP 8 recommended coding style."""

import re
import sys

import requests



DISCOVERY_URL = "https://www.googleapis.com/discovery/v1/apis/youtube/v3/rest"



def str_index_set(haystack, needles, start=None, end=None, /, **kwargs):
    """Like str.index, but finds the first index in haystack where one of the
    needed is located."""

    idx = None
    for needle in needles:
        try:
            i = haystack.index(needle, start, end)
        except ValueError:
            continue
        if idx is None or idx > i:
            idx = i

    if idx is not None:
        return idx
    if "default" in kwargs:
        return kwargs["default"]
    raise ValueError("substring not found")



def str_rindex_set(haystack, needles, start=None, end=None, /, **kwargs):
    """Like str.rindex, but finds the last index in haystack where one of the
    needed is located."""

    idx = None
    for needle in needles:
        try:
            i = haystack.rindex(needle, start, end)
        except ValueError:
            continue
        if idx is None or idx < i:
            idx = i

    if idx is not None:
        return idx
    if "default" in kwargs:
        return kwargs["default"]
    raise ValueError("substring not found")



class OnlyRepr:
    # pylint: disable=too-few-public-methods
    """This class only implement __repr__ and is used for pretty_str below. It
    allows to explicitly set the repr(...) of an object."""

    def __init__(self, s):
        self.repr_str = s

    def __repr__(self):
        return self.repr_str



def _pretty_str_str(obj, width=80, indent_pad="    ", level=0,
                    first_line_len=None, cont_str=" \\", cont_pad=""):
    # pylint: disable=too-many-arguments,too-many-positional-arguments
    sp = indent_pad * level
    r = ""
    if first_line_len is None:
        r += sp
        first_line_len = len(sp)

    obj_repr = repr(obj)
    rtmp = r + obj_repr
    if len(rtmp) <= width - first_line_len or not isinstance(obj, (str, bytes, bytearray)):
        return rtmp

    # These types are decoorated with some quote and other things.
    # And all end with the cont_str string.
    decor_len = len(repr(type(obj)())) + len(cont_str)

    l0 = wrap(obj[:width], width - first_line_len - decor_len, strip=False)[0]
    r += repr(l0)
    r += cont_str + "\n"
    lines = wrap(obj[len(l0):], width - len(sp) - decor_len - len(cont_pad), strip=False)
    r += (cont_str + "\n").join(sp + cont_pad + repr(l) for l in lines)
    return r



def _pretty_str_dict(obj, width=80, indent_pad="    ", level=0, first_line_len=None):
    sp = indent_pad * level
    r = ""
    if first_line_len is None:
        r += sp
        first_line_len = len(sp)

    r += "{\n"

    for k, v in obj.items():
        r += pretty_str(k, width, indent_pad, level + 1, cont_str="",
                        cont_pad=indent_pad)
        r += ": "

        last_line_len = len(r.rsplit("\n", maxsplit=1)[-1])
        cont_pad_len = last_line_len - first_line_len - len(indent_pad)

        r += pretty_str(v, width, indent_pad, level + 1, first_line_len=last_line_len,
                        cont_str="", cont_pad=" " * cont_pad_len)
        r += ",\n"

    r += sp + "}"

    return r



def _pretty_str_list_oneline(obj, width=80, indent_pad="    ", level=0, first_line_len=None):
    if isinstance(obj, list):
        op, cl = "[", "]"
    elif isinstance(obj, tuple):
        op, cl = "(", ")"
    else:
        raise TypeError("_pretty_str_list can't pretty print a {type(obj)}")

    sp = indent_pad * level
    r = ""
    if first_line_len is None:
        r += sp
        first_line_len = len(sp)

    r += op

    for v in obj:
        last_line_len = len(r.rsplit("\n", maxsplit=1)[-1])
        if "\n" not in r:
            last_line_len += first_line_len
        vstr = pretty_str(v, width, indent_pad, level, first_line_len=last_line_len,
                        cont_str="")

        # If the element v is on several lines, try again with one element per line
        if "\n" in vstr:
            return None

        r += vstr
        r += ", "

    r = r.removesuffix(", ") + cl

    return r



def _pretty_str_list_multiline(obj, width=80, indent_pad="    ", level=0, first_line_len=None):
    if isinstance(obj, list):
        op, cl = "[", "]"
    elif isinstance(obj, tuple):
        op, cl = "(", ")"
    else:
        raise TypeError("_pretty_str_list can't pretty print a {type(obj)}")

    sp = indent_pad * level
    r = ""
    if first_line_len is None:
        r += sp
        first_line_len = len(sp)

    r += op + "\n"

    for v in obj:
        r += pretty_str(v, width, indent_pad, level + 1, cont_str="")
        r += ",\n"

    r = r + sp + cl
    return r



def _pretty_str_default(obj, indent_pad="    ", level=0, first_line_len=None):
    # Passer sp et r, et virer indent_pad et level
    sp = indent_pad * level
    r = ""
    if first_line_len is None:
        r += sp

    return r + repr(obj)



def pretty_str(obj, width=80, indent_pad="    ", level=0, first_line_len=None,
               cont_str=" \\", cont_pad=""):
    # pylint: disable=too-many-arguments,too-many-positional-arguments
    """This function exists because the module pprint produce a shitty format
    and shouldn't even exist.
    Note that the wraping of long strings to fit some width is not perfect and
    will miss the backslash-escaped characters for instance.

    Arguments are:
    - obj: the object to return the pretty string for
    - width: how wide the text should be, currently, only str and bytes are split
    - indent_pad: the indentation string, usually 4 spaces or a tab
    - level: the current indentation level
    - first_line_len: if the returnd string isn't pasted at the beginning of a
      line, this should be the length of the string already existing, or None
      if the first line should be indented
    - cont_str: continuation string to use when wraping long strings, usually a
      backslash or an empty string if the context (inside parentheses for
      instance) allows juxtaposed strings
    - cont_pad: string for additional indentation of continuation."""

    if isinstance(obj, (str, int, float, complex, bytes, bytearray)):
        return _pretty_str_str(obj, width, indent_pad, level, first_line_len, cont_str, cont_pad)

    if isinstance(obj, dict):
        return _pretty_str_dict(obj, width, indent_pad, level, first_line_len)

    if isinstance(obj, (list, tuple)):
        s = _pretty_str_list_oneline(obj, width, indent_pad, level, first_line_len)
        if s is None:
            s = _pretty_str_list_multiline(obj, width, indent_pad, level, first_line_len)
        return s

    return _pretty_str_default(obj, indent_pad, level, first_line_len)



def wrap(text, width=80, seps=" ", strip=True):
    """Wraps a text string to `width' columns on separators `seps'."""

    if width < 1:
        raise ValueError(f"Invalid width {width}, must be >= 1")

    if len(text) == 0:
        return [""]

    ret = []
    while text:
        if len(text) <= width:
            idx = len(text)
        else:
            idx = str_rindex_set(text, seps, 0, width - 1, default=None)
            if idx is None:
                idx = str_index_set(text, seps, width - 1, default=len(text))

            # Keep the separator at the end of the line
            idx += 1

        ret.append(text[:idx])
        text = text[idx:]

        if strip:
            ret[-1] = ret[-1].rstrip(seps)
            text = text.lstrip(seps)

    return ret



def format_docstr(s, levels=1):
    """Format a multiline string to be a docstring.

    Namely this function:
    - Prepend and append three double-quote
    - Wrap the long lines so that the text fit on 80 columns including the
      indentation
    - Lines starting with "- " have an added two spaces on the continuation
      (see above and here)
    - Prepend levels*4 spaces on each lines."""

    w = levels * 4
    sp = " " * w

    retval = ""
    for line in f'"""{s}"""'.splitlines():
        wtmp = w
        sptmp = sp

        # Handle the list items specially. Add 2 spaces on continuation lines.
        if line.startswith("- "):
            l = wrap(line, 80 - w)[0]
            if retval:
                retval += "\n"
            retval += sp + l
            line = line.removeprefix(l).lstrip()
            if line == "":
                continue
            wtmp += 2
            sptmp += "  "

        # Normal lines (not starting with "- " and continuations are handled here
        for l in wrap(line, 80 - wtmp):
            if retval:
                retval += "\n"
            if l:
                retval += sptmp
            retval += l

    return retval



def escape_builtin(name):
    if hasattr(__builtins__, name):
        name += "_"
    return name



def camel_case_to_python(camel, escape_builtins=True):
    """Convert a camelCase name into a snake_case name. Also prevent overriding
    some python builtin by appending an underscore."""

    newname = re.sub(r"([a-z])([A-Z]+)", r"\1_\2", camel).lower()

    if escape_builtins:
        newname = escape_builtin(newname)
    return newname



def gen_method_doc(api_help):
    """Generate the docstring of a method."""

    def params_help(params):
        ret = ""
        for p in params:
            if p["help"] is not None:
                ret += f"- {p['name']}: {p['type']}: {p['help']}\n"
            else:
                ret += f"- {p['name']}: {p['type']}\n"
        return ret

    doc = api_help["help"] + "\n"

    if api_help["required_params"]:
        doc += "\nRequired arguments:\n"
        doc += params_help(api_help["required_params"])

    if api_help["optional_params"]:
        doc += "\nOptional arguments:\n"
        doc += params_help(api_help["optional_params"])

    return format_docstr(doc, levels=2)



def gen_api_help(meth, named_args, optional_args, params_style_conv):
    """Generate the dict describing the method and its arguments."""

    def param_help(params, name):
        n = params_style_conv.get(name, name)
        p = params[n]
        return {
            "name": name,
            "type": p["type"],
            "help": p.get("description"),
            "deprecated": p.get("deprecated", False),
        }

    params = meth["parameters"]
    retval = {"help": meth["description"]}
    retval["required_params"] = [param_help(params, p) for p in named_args]
    retval["optional_params"] = [param_help(params, p) for p in optional_args]
    retval["method"] = NotImplemented

    # Fully-Qualified Method Name. :]
    retval["FQMN"] = [camel_case_to_python(n, False) for n in meth["id"].split(".")]

    return retval



def gen_code_for_method(meth, is_first, fp):
    """Generate the code for a method as described in the JSON provided by the
    discovery URL."""

    meth_name = "_".join(meth["id"].split(".")[1:])
    meth_name = camel_case_to_python(meth_name)

    params = meth["parameters"]

    # Conversion frm camelCase to snake_case pf parameters
    params_style_conv = {camel_case_to_python(n): n for n in sorted(params)}
    params_style_conv = {k: v for k, v in params_style_conv.items() if k != v}

    # These are the arguments explicited required for the generated functions
    required_params = {n: p for n, p in params.items() if p.get("required", False)}
    named_args = meth["parameterOrder"]
    named_args += sorted(set(required_params) - set(named_args))
    optional_args = sorted(set(params) - set(named_args))

    # Convert those names to pythonic snake_case
    named_args = [camel_case_to_python(n) for n in named_args]
    optional_args = [camel_case_to_python(n) for n in optional_args]

    # Parameters passed by location require a special handling in the code
    path_params = {n: p for n, p in params.items() if p["location"] == "path"}

    # Build the strings used in the code
    named_args_str = ", ".join(named_args)
    if named_args_str:
        named_args_str += ", "
    named_args_dict = ", ".join(f"{n!r}: {n}" for n in named_args)
    named_args_dict = "{" + named_args_dict + "}"

    params_style_conv_str = "\n".join(" " * 12 + f"{k!r}: {v!r}," for k, v in params_style_conv.items())
    params_style_conv_str = "{\n" + params_style_conv_str + "\n        }"

    # The method and path to call
    method = meth["httpMethod"].lower()
    path = meth["flatPath"].removeprefix("youtube/v3/")

    # Build the docstring
    api_help = gen_api_help(meth, named_args, optional_args, params_style_conv)
    api_help["method"] = OnlyRepr(meth_name)
    doc = gen_method_doc(api_help)

    # Finally, output the code
    print(file=fp)
    if not is_first:
        print(file=fp)
        print(file=fp)

    print(f"    def {meth_name}(self, {named_args_str}request_args=None, **kwargs):", file=fp)
    print(doc, file=fp)

    print(file=fp)
    print("        if request_args is None:", file=fp)
    print("            request_args = {}", file=fp)
    print(f"        kwargs.update({named_args_dict})", file=fp)
    if params_style_conv:
        print(f"        style_conv = {params_style_conv_str}", file=fp)
        print("        kwargs = {style_conv.get(k, k): v for k, v in kwargs.items()}", file=fp)
    if path_params:
        print('        # pylint: disable=consider-using-f-string', file=fp)
        print(f'        path = {path!r}.format(**kwargs)', file=fp)
        print(f"        return self.{method}(path, params=kwargs)", file=fp)
    else:
        print(f"        return self.{method}({path!r}, params=kwargs, **request_args)", file=fp)

    # Return informations to build the API help dict
    return meth_name, api_help



# pylint: disable=missing-function-docstring
def main():
    if len(sys.argv) != 2:
        print(f"usage: {sys.argv[0]} outputfilename")
        return 1

    outfile = sys.argv[1]
    if "generated" not in outfile or not outfile.endswith(".py"):
        print("Output filename must contain 'generated' end with .py", file=sys.stderr)
        return 2

    res = requests.get(DISCOVERY_URL, timeout=60)
    res.raise_for_status()
    desc = res.json()

    with open(outfile, "w") as fp:
        print(format_docstr("File generated with: " + " ".join(sys.argv), levels=0), file=fp)
        print(file=fp)
        print(f'class {desc["canonicalName"]}Mixin:', file=fp)
        print("    # pylint: disable=too-many-public-methods,too-many-lines", file=fp)
        print(format_docstr(f'{desc["title"]}\n\n{desc["description"]}'), file=fp)

        api_help = {}
        first = True
        for resname in sorted(desc["resources"]):
            res = desc["resources"][resname]
            if "methods" not in res:
                print(f"Skipping the weirdly formatted resource {resname}:", res, file=sys.stderr)
                continue

            for methname in sorted(res["methods"]):
                method = res["methods"][methname]
                name, api_meth_help = gen_code_for_method(method, first, fp)
                api_help[name] = api_meth_help
                first = False

        print(file=fp)
        print(file=fp)
        print(file=fp)
        s = "    api_help = "
        print(s + pretty_str(api_help, level=1, first_line_len=len(s)), file=fp)

    return 0



if __name__ == "__main__":
    sys.exit(main())
