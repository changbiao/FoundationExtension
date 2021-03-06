from NSAttributedStringData import *

implnumber = """{availableheader}
//! Generated by {filename}
- (NSNumber *){name}Number {{ return [self objectForKey:NS{Name}AttributeName]; }}
//! Generated by {filename}
- (void)set{Name}Number:(NSNumber *){name}Number {{ [self setObject:{name}Number forKey:NS{Name}AttributeName]; }}
{availablefooter}"""

implscalar = """{availableheader}
//! Generated by {filename}
- ({type}){name} {{ return [self.{name}Number {number}Value]; }}
//! Generated by {filename}
- (void)set{Name}:({type}){name} {{ self.{name}Number = [NSNumber numberWith{Number}:{name}]; }}
{availablefooter}"""

impl = """{availableheader}
//! Generated by {filename}
- ({type}){name} {{ return [self objectForKey:NS{Name}AttributeName]; }}
//! Generated by {filename}
- (void)set{Name}:({type}){name} {{ [self setObject:{name} forKey:NS{Name}AttributeName]; }}
{availablefooter}"""

for prop in props:
    if prop.has_impl: continue
    if prop.has_number:
        print implnumber.format(
                name=prop.name,
                Name=prop.Name,
                filename=__file__,
                availableheader=prop.available_header if prop.available else '',
                availablefooter='#endif' if prop.available else '',
            )
        if prop.name == 'ligature': continue
        print implscalar.format(
            attr=prop.proptype,
            type=prop.type,
            typespace='' if prop.is_pointer else ' ',
            name=prop.name,
            filename=__file__,
            Name=prop.Name,
            number=prop.number,
            Number=prop.Number,
            availableheader=prop.available_header if prop.available else '',
            availablefooter='#endif' if prop.available else '',
            )
    else:
        print impl.format(
            attr=prop.proptype,
            type=prop.type,
            typespace='' if prop.is_pointer else ' ',
            name=prop.name,
            filename=__file__,
            Name=prop.Name,
            number=prop.number,
            Number=prop.Number,
            availableheader=prop.available_header if prop.available else '',
            availablefooter='#endif' if prop.available else '',
        )

