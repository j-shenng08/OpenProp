from pathlib import Path

folder = r"OpenProp_v3.3.4\Prop1_SolidWorks_v18" ##Change this

for path in Path(folder).glob("SectionCurve*.txt"):
    num = int(path.stem.replace("SectionCurve", ""))
    path.rename(path.with_name(f"SectionCurve{num:02d}.py"))