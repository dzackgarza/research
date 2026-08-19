# Chapter 2 — Triangle Groups and Translation Subgroups

> Source: https://www.hypercells.net/HyperCells/doc/chap2_mj.html

## 2.1 Triangle Groups

Triangle groups are stored as objects of category `TriangleGroup`. Characterized by signature (r,q,p) in ascending order:

Δ(r,q,p) = ⟨a,b,c | a², b², c², (ab)ʳ, (bc)^q, (ca)^p⟩

Proper triangle groups stored as `ProperTriangleGroup`:

Δ⁺(r,q,p) = ⟨x,y,z | xyz, xʳ, y^q, z^p⟩

where x = ab, y = bc, z = ca.

### 2.1-1 TriangleGroup( signature )
Returns a `TriangleGroup` object. Construct with signature `[r, q, p]`. Generators named `a`, `b`, `c`.

### 2.1-2 ProperTriangleGroup( signature )
Returns a `ProperTriangleGroup` object. Construct with signature `[r, q, p]`. Generators named `x`, `y`, `z`.

### 2.1-3 Signature( tg )
Returns the signature of the triangle group.

### 2.1-4 FpGroup( tg )
Returns the triangle group as a finitely presented group.

## 2.2 Translation Groups

### 2.2-1 TGTranslationGroupFromQuotient( D, G, genus [, GAMgens [, TDGAM [, TGGw ]]] )
Constructs translation group from quotient data.

### 2.2-2 TGTranslationGroup( tg, quotient )
Constructs translation group from triangle group and quotient.

### 2.2-3 GetProperTriangleGroup( Gamma )
Returns the proper triangle group Δ⁺ of which the translation group Gamma is a subgroup.

### 2.2-4 QuotientHomomorphism( Gamma )
Returns the group homomorphism from Δ⁺ to Δ⁺/Γ.

### 2.2-5 AsTGSubgroup( Gamma )
Returns the translation group as a subgroup of Δ⁺.

### 2.2-6 FpGroup( Gamma )
Returns the translation group as a finitely presented group with generators `g1`, `g2`, ....

### 2.2-7 FpIsomorphism( Gamma )
Returns the group isomorphism from `AsTGSubgroup(Gamma)` to `FpGroup(Gamma)`.

## 2.3 Triangle-Group Quotients

### 2.3-1 TGQuotient( quotient [, signature ] )
Constructs a triangle-group quotient.

### 2.3-2 TGQuotientName( tgquotient )
Returns the name of the quotient.

### 2.3-3 TGQuotientGenus( tgquotient )
Returns the genus.

### 2.3-4 TriangleGroupSignature( tgquotient )
Returns the signature.

### 2.3-5 TGQuotientOrder( tgquotient )
Returns the order of the quotient.

### 2.3-6 TGQuotientActionType( tgquotient )
Returns the action type: `"reflexible [m]"`, `"reflexible [n]"`, or `"chiral"`.

### 2.3-7 TGQuotientRelators( tgquotient )
Returns the defining relators as a string.

### 2.3-8 TGQuotientRelators( tg, tgquotient )
Returns relators as elements of the triangle group.

### 2.3-9 TGQuotientGroup( tg, tgquotient )
Returns the quotient group.

## 2.4 Library of Triangle-Group Quotients

Based on Marston Conder's list of quotients acting on surfaces of genus 2 to 101.
Labeled by genus `g` and running index `n`: `Tg.n`.

### 2.4-1 LoadTGQuotients( signature )
Loads quotients for a given signature.

### 2.4-2 ListTriangleGroups( arg )
Lists available triangle groups.

### 2.4-3 ListTGQuotients( signature )
Lists available quotients for a signature.

## 2.5 Export and Import

### 2.5-1 ExportString( tgquotient )
Returns a string for export.

### 2.5-2 ImportTGQuotientString( string )
Constructs a `TGQuotient` from an export string.
