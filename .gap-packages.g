#!/usr/bin/env gap

BindGlobal("DZACK_RESEARCH_InstallComplexPackages", function()
local IsExactPackageInstalled, packages, package, required;

if LoadPackage("PackageManager") <> true then
    PrintTo("*errout*", "PackageManager is required\n");
    QUIT_GAP(1);
fi;

PKGMAN_SetCustomPackageDir(Filename(DirectoryCurrent(), ".gap/pkg"));

IsExactPackageInstalled := function(package)
    return ForAny(
        PKGMAN_UserPackageInfo(package[1]),
        info -> info.Version = package[2]
    );
end;

packages := [
    [ "RingsForHomalg", "2026.05-01", "https://github.com/homalg-project/homalg_project/releases/download/RingsForHomalg-2026.05-01/RingsForHomalg-2026.05-01.tar.gz" ],
    [ "CAP", "2026.07-04", "https://github.com/homalg-project/CAP_project/releases/download/CAP-2026.07-04/CAP-2026.07-04.tar.gz" ],
    [ "ModulePresentationsForCAP", "2026.06-01", "https://github.com/homalg-project/CAP_project/releases/download/ModulePresentationsForCAP-2026.06-01/ModulePresentationsForCAP-2026.06-01.tar.gz" ]
];
for package in packages do
    required := Concatenation("=", package[2]);
    if not IsExactPackageInstalled(package) then
        if InstallPackage(package[3]) <> true then
            PrintTo("*errout*", "failed to install ", package[1], " ", package[2], "\n");
            QUIT_GAP(1);
        fi;
    fi;
    if not IsExactPackageInstalled(package) then
        PrintTo("*errout*", "package is not installed locally: ", package[1], " ", package[2], "\n");
        QUIT_GAP(1);
    fi;
    if LoadPackage(package[1], required) <> true then
        PrintTo("*errout*", "failed to load ", package[1], " ", package[2], "\n");
        QUIT_GAP(1);
    fi;
od;
end);

CallFuncList(ValueGlobal("DZACK_RESEARCH_InstallComplexPackages"), []);
MakeReadWriteGlobal("DZACK_RESEARCH_InstallComplexPackages");
UnbindGlobal("DZACK_RESEARCH_InstallComplexPackages");
QUIT_GAP(0);
